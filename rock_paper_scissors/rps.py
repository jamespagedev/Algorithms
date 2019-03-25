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
    def get_unused_play(play, exponentNumber):
        for hand in rps:
            play.append(hand)
            if exponentNumber == n:
                possible_plays.append(play)
            else:
                get_unused_play(play, exponentNumber + 1)

            # https://medium.com/@junshengpierre/recursion-rockpaperscissors-js-b071a334080a
            # debug later, move onto next problem

    # call recursive helper method
    get_unused_play([], 1)

    # return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
