#!/usr/bin/env python3
from time import sleep, time
import argparse
import random
import sys


generation = 0
start_time = time()


def is_binary_string(string):
    for character in string:
        if character != "0" and character != "1":
            return False
    return True


def build_rules(number):
    bits = "{0:b}".format(number).zfill(8)
    return {
        "111": bits[0],
        "110": bits[1],
        "101": bits[2],
        "100": bits[3],
        "011": bits[4],
        "010": bits[5],
        "001": bits[6],
        "000": bits[7],
    }


def update_state(state, rules, wrap):
    new_state = ""
    for i in range(0, len(state)):
        center_cell = state[i]
        if wrap:
            left_cell = state[i - 1] if (i > 0) else state[len(state) - 1]  # wraps
            right_cell = state[i + 1] if (i + 1 < len(state)) else state[0]  # wraps
        else:
            left_cell = state[i - 1] if (i > 0) else "0"  # no-wrap
            right_cell = state[i + 1] if (i + 1 < len(state)) else "0"  # no-wrap
        new_state += rules[left_cell + center_cell + right_cell]
    return new_state


def render(value, generation, off_char, on_char):
    output = value.replace("0", off_char).replace("1", on_char)
    if generation != -1:
        output = output + "|" + str(generation)
    print(output)


def render_stats():
    global generation
    global start_time
    print("🤖📈 Stats:")
    print("Generation(s) calculated: " + str(generation))
    print("Duration: " + str(time() - start_time) + " seconds")


def main(args):
    global generation

    # validate args
    if args.rule is not None and (args.rule < 0 or args.rule > 255):
        sys.exit("🤖🔥 Error: --rule must be between 0 and 255, inclusive.")
    if args.state is not None and args.random is not None:
        sys.exit("🤖🔥 Error: Do not set --state and --random at the same time.")
    if args.start < 0:
        sys.exit("🤖🔥 Error: --start must be a positive number or 0.")
    if args.end != -1 and args.limit != 0:
        sys.exit("🤖🔥 Error: Do not set --end and --limit at the same time.")
    if args.end < args.start and args.end != -1:
        sys.exit("🤖🔥 Error: --end must be equal to greater than --start (or -1).")
    if args.limit < 0:
        sys.exit("🤖🔥 Error: --limit must be a positive number.")

    # random seed
    if args.seed is not None:
        random.seed(args.seed)

    # generate rules
    rule = args.rule
    if args.random_rule:
        rule = random.randint(0, 255)
        print("🤖🎲 Picked rule " + str(rule))
    rules = build_rules(rule)

    # initial state
    state = ""
    if args.state is not None:
        state = args.state
    elif args.random is not None:
        for i in range(0, args.random):
            state = str(random.randint(0, 1)) + state
    while not state or not is_binary_string(state):
        state = input("🤖 Enter an initial string of ones and zeroes:\n")

    # padding initial state
    required_padding = max(args.pad - len(state), 0)
    side = args.pad_side
    for i in range(0, required_padding):
        if side == "left" or (side == "both" and i % 2 == 0):
            state = "0" + state
        elif side == "right" or (side == "both" and i % 2 == 1):
            state = state + "0"

    # characters for console rendering
    off_char = args.off[0]
    on_char = args.on[0]

    # wrapping
    wrap = args.wrap

    # rendering range
    show_from = args.start
    stop_at = args.end
    if stop_at == -1 and args.limit != 0:
        stop_at = show_from + args.limit - 1

    # loop
    delay = args.delay / 1000
    while True:
        if generation >= show_from:
            sleep(delay)
            render(state, generation if args.counter else -1, off_char, on_char)
        if stop_at != -1 and generation >= stop_at:
            if args.show_stats:
                render_stats()
            sys.exit(0)
        state = update_state(state, rules, wrap)
        generation = generation + 1


parser = argparse.ArgumentParser()
parser.add_argument(
    "state",
    metavar="STATE",
    type=str,
    nargs="?",
    help="set the initial state (e.g. 01101110)",
)
parser.add_argument(
    "-r",
    "--rule",
    default=110,
    help="set the rule to use (between 0 to 255, inclusive). defaults to rule 110",
    type=int,
)
parser.add_argument(
    "-p",
    "--pad",
    default=0,
    help="pads the initial state (with zeroes) to this length (e.g. --pad=20)",
    type=int,
)
parser.add_argument(
    "-d",  # for direction...
    "--pad-side",
    default="left",
    help="set which side to pad the initial state: left (default), right, or both",
    choices=["left", "right", "both"],
)
parser.add_argument(
    "--delay",
    default=250,
    help="delay between displaying each generation in milliseconds (defaults to"
    " 250 ms)",
    type=int,
)
parser.add_argument(
    "--counter", dest="counter", action="store_true", help="show the iteration count"
)
parser.set_defaults(counter=False)
parser.add_argument(
    "--off",
    help="character to show when a cell is off (defaults to a blank space)",
    default=" ",
    type=str,
)
parser.add_argument(
    "--on",
    help="character to show when a cell is on (defaults to X)",
    default="X",
    type=str,
)
parser.add_argument(
    "--random", help="generate random starting state of N length", type=int
)
parser.add_argument(
    "--random-rule",
    dest="random_rule",
    action="store_true",
    help="pick a rule at random",
)
parser.set_defaults(random_rule=False)
parser.add_argument(
    "--seed", help="set the base seed for the random number generator", type=int
)
parser.add_argument(
    "--no-wrap", dest="wrap", action="store_false", help="prevent edges wrapping"
)
parser.set_defaults(wrap=True)
parser.add_argument(
    "-s",
    "--start",
    default=0,
    help="set the generation to start rendering from, inclusive (e.g. --start 10). initial state is generation 0.",
    type=int,
)
parser.add_argument(
    "-e",
    "--end",
    default=-1,
    help="set generation to stop at (-1 = unlimited). must be equal or greater than --start if set.",
    type=int,
)
parser.add_argument(
    "-l",
    "--limit",
    default=0,
    help="set maximum number of generations to render (0 = unlimited). similar to --end.",
    type=int,
)
parser.add_argument(
    "--stats",
    dest="show_stats",
    action="store_true",
    help="output stats on exit",
)
parser.set_defaults(show_stats=False)

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        if args.show_stats:
            render_stats()
        sys.exit(0)
