#!/usr/bin/env python3
from time import sleep
import argparse
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


def update_state(state):
    value = ''
    for i in range(0, len(state)):
        l = state[i - 1] if (i > 0) else state[len(state) - 1]  # wraps
        c = state[i]
        r = state[i + 1] if (i + 1 < len(state)) else state[0]  # wraps
        value += get_value(l, c, r)
    return value


def render(value, off_char, on_char):
    print(value.replace('0', off_char).replace('1', on_char))


def main(args):
    # initial state
    state = args.state
    while not state or not is_binary_string(state):
        state = input('🤖 Enter an initial string of ones and zeroes:\n')

    # left padding initial state
    required_padding = max(args.pad_left - len(state), 0)
    for i in range(0, required_padding):
        state = '0' + state

    # characters for console rendering
    off_char = args.off[0]
    on_char = args.on[0]

    # loop
    render(state, off_char, on_char)
    while True:
        state = update_state(state)
        render(state, off_char, on_char)
        sleep(0.25)


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--state', help='set the initial state (e.g. --state 01101110)', type=str)
parser.add_argument('-p', '--pad-left', default=0, help='pads the initial state (wtih zeroes) to this length '
                                                        '(e.g. --pad-left=20)', type=int)
parser.add_argument('--off', help='character to show when a cell is off (e.g. default is a blank space)', default=' ',
                    type=str)
parser.add_argument('--on', help='character to show when a cell is on (e.g. default is X)', default='X',
                    type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    try:
        main(args)
    except KeyboardInterrupt:
        sys.exit(0)
