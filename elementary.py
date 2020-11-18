#!/usr/bin/env python3
from time import sleep
import argparse


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


def render(value):
    print(value.replace('0', ' ').replace('1', 'X'))


def main(args):
    # initial state
    state = args.state
    while not state or not is_binary_string(state):
        state = input("🤖 Enter an initial string of ones and zeroes: ")

    # left padding initial state
    required_padding = max(args.pad_left - len(state), 0)
    for i in range(0, required_padding):
        state = '0' + state

    # loop
    render(state)
    while True:
        state = update_state(state)
        render(state)
        sleep(0.25)


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--state", help="set the initial state (e.g. --state 01101110)", type=str)
parser.add_argument("-p", "--pad-left", default=0, help="pads the initial state (wtih zeroes) to this length "
                                                        "(e.g. --pad-left=20)", type=int)

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
