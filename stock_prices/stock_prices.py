#!/usr/bin/python

import argparse


def find_max_profit(prices):
    min_loss = 0
    loss = 0
    max_profit = 0
    increase = 0
    starting_point = prices[0]

    for i, price in enumerate(prices):
        if i < (len(prices) - 1) and price > prices[i+1]:  # drop
            starting_point = prices[i+1]
            loss = prices[i+1] - price
            if min_loss == 0:
                min_loss = loss
            elif min_loss < loss:
                min_loss = loss
        if i < (len(prices) - 1) and price < prices[i+1]:  # rise
            increase = prices[i+1] - starting_point
            if increase > max_profit:
                max_profit = increase

    if max_profit == 0:
        return min_loss
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
