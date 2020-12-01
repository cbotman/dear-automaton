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


def get_value(l, c, r):
    rules = {
        '111': '0',
        '110': '1',
        '101': '1',
        '100': '0',
        '011': '1',
        '010': '1',
        '001': '1',
        '000': '0',
    }
    return rules[l + c + r]


def update_state(state, wrap):
    new_state = ''
    for i in range(0, len(state)):
        center_cell = state[i]
        if wrap:
            left_cell = state[i - 1] if (i > 0) else state[len(state) - 1]  # wraps
            right_cell = state[i + 1] if (i + 1 < len(state)) else state[0]  # wraps
        else:
            left_cell = state[i - 1] if (i > 0) else '0'  # no-wrap
            right_cell = state[i + 1] if (i + 1 < len(state)) else '0'  # no-wrap
        new_state += get_value(left_cell, center_cell, right_cell)
    return new_state


def render(value, generation, off_char, on_char):
    output = value.replace('0', off_char).replace('1', on_char)
    if generation != -1:
        output = output + '|' + str(generation)
    print(output)


def main(args):
    # validate args
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

    # left padding initial state
    required_padding = max(args.pad_left - len(state), 0)
    for i in range(0, required_padding):
        state = '0' + state

    # characters for console rendering
    off_char = args.off[0]
    on_char = args.on[0]

    # wrapping
    wrap = args.wrap

    # loop
    generation = 0
    delay = args.delay / 1000
    while True:
        render(state, generation if args.counter else -1, off_char, on_char)
        state = update_state(state, wrap)
        generation = generation + 1
        sleep(delay)


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--state', help='set the initial state (e.g. --state 01101110)', type=str)
parser.add_argument('-p', '--pad-left', default=0, help='pads the initial state (wtih zeroes) to this length '
                                                        '(e.g. --pad-left=20)', type=int)
parser.add_argument('-d', '--delay', default=250, help='delay between displaying each generation in milliseconds',
                    type=int)
parser.add_argument('--counter', dest='counter', action='store_true', help='show the iteration count')
parser.set_defaults(counter=False)
parser.add_argument('--off', help='character to show when a cell is off (e.g. default is a blank space)', default=' ',
                    type=str)
parser.add_argument('--on', help='character to show when a cell is on (e.g. default is X)', default='X',
                    type=str)
parser.add_argument('-r', '--random', help='generate random starting state of N length', type=int)
parser.add_argument('--seed', help='set the base seed for the random number generator', type=int)
parser.add_argument('--no-wrap', dest='wrap', action='store_false', help='prevent edges wrapping')
parser.set_defaults(wrap=True)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(0)
