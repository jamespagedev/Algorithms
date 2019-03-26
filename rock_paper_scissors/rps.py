#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    # edge case n == 0, return [[]]
    if n == 0:
        return [[]]

    # edge case n == 1, return [['rock'], ['paper'], ['scissors']]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]

    # general case...

    # Assign rock, paper, scissors to an array(rps)
    rps = ['rock', 'paper', 'scissors']

    # instantiate an empty array called possible_plays
    possible_plays = []

    # use a recursive helper method called get_unused_play
    def get_unused_play(exponent, combos):
        if exponent == 0:
            possible_plays.append(combos)
            return

        for hand in rps:
            get_unused_play(exponent - 1, combos + [hand])

    # call recursive helper method
    get_unused_play(n, [])

    # return possible_plays
    return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
