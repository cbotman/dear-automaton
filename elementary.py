#!/usr/bin/env python3
from time import sleep
import argparse
import random
import sys


def is_binary_string(string):
    for character in string:
        if character != '0' and character != '1':
            return False
    return True


def build_rules(number):
    bits = "{0:b}".format(number).zfill(8)
    return {
        '111': bits[0],
        '110': bits[1],
        '101': bits[2],
        '100': bits[3],
        '011': bits[4],
        '010': bits[5],
        '001': bits[6],
        '000': bits[7],
    }


def update_state(state, rules, wrap):
    new_state = ''
    for i in range(0, len(state)):
        center_cell = state[i]
        if wrap:
            left_cell = state[i - 1] if (i > 0) else state[len(state) - 1]  # wraps
            right_cell = state[i + 1] if (i + 1 < len(state)) else state[0]  # wraps
        else:
            left_cell = state[i - 1] if (i > 0) else '0'  # no-wrap
            right_cell = state[i + 1] if (i + 1 < len(state)) else '0'  # no-wrap
        new_state += rules[left_cell + center_cell + right_cell]
    return new_state


def render(value, generation, off_char, on_char):
    output = value.replace('0', off_char).replace('1', on_char)
    if generation != -1:
        output = output + '|' + str(generation)
    print(output)


def main(args):
    # validate args
    if args.rule is not None and (args.rule < 0 or args.rule > 255):
        sys.exit('🤖🔥 Error: --rule must be between 0 and 255, inclusive.')
    if args.state is not None and args.random is not None:
        sys.exit('🤖🔥 Error: Do not set --state and --random at the same time.')

    # initial state
    state = ''
    if args.state is not None:
        state = args.state
    elif args.random is not None:
        if args.seed is not None:
            random.seed(args.seed)
        for i in range(0, args.random):
            state = str(random.randint(0, 1)) + state
    while not state or not is_binary_string(state):
        state = input('🤖 Enter an initial string of ones and zeroes:\n')

    # padding initial state
    required_padding = max(args.pad - len(state), 0)
    direction = args.pad_dir
    for i in range(0, required_padding):
        if direction == 'left' or (direction == 'both' and i % 2 == 0):
            state = '0' + state
        elif direction == 'right' or (direction == 'both' and i % 2 == 1):
            state = state + '0'

    # characters for console rendering
    off_char = args.off[0]
    on_char = args.on[0]

    # rules
    rules = build_rules(args.rule)
    wrap = args.wrap

    # loop
    generation = 0
    delay = args.delay / 1000
    while True:
        render(state, generation if args.counter else -1, off_char, on_char)
        state = update_state(state, rules, wrap)
        generation = generation + 1
        sleep(delay)


parser = argparse.ArgumentParser()
parser.add_argument('-r', '--rule', default=110, help='set the rule to use (between 0 to 255, inclusive). defaults to '
                                                      'rule 110', type=int)
parser.add_argument('-s', '--state', help='set the initial state (e.g. --state 01101110)', type=str)
parser.add_argument('-p', '--pad', default=0, help='pads the initial state (with zeroes) to this length (e.g. --pad=20)'
                    , type=int)
parser.add_argument('-d', '--pad-dir', default='left', help='sets how to apply padding: left (default), right, or both',
                    choices=['left', 'right', 'both'])
parser.add_argument('--delay', default=250, help='delay between displaying each generation in milliseconds (defaults to'
                                                 ' 250 ms)',
                    type=int)
parser.add_argument('--counter', dest='counter', action='store_true', help='show the iteration count')
parser.set_defaults(counter=False)
parser.add_argument('--off', help='character to show when a cell is off (defaults to a blank space)', default=' ',
                    type=str)
parser.add_argument('--on', help='character to show when a cell is on (defaults to X)', default='X',
                    type=str)
parser.add_argument('--random', help='generate random starting state of N length', type=int)
parser.add_argument('--seed', help='set the base seed for the random number generator', type=int)
parser.add_argument('--no-wrap', dest='wrap', action='store_false', help='prevent edges wrapping')
parser.set_defaults(wrap=True)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(0)
