#!/usr/bin/python

import sys
import math

"""
For example, `making_change(10)` should return 4, since there are 4 ways to make change for 10 cents using pennies, nickels, dimes, quarters, and half-dollars:

 1. We can make change for 10 cents using 10 pennies
 2. We can use 5 pennies and a nickel
 3. We can use 2 nickels
 4. We can use a single dime
"""
# h = 50  # half-dollar
# q = 25  # quarter
# d = 10  # dime
# n = 5  # nickel
# p = 1  # penny
# coin_types = [h, q, d, n, p]
# coin_counts = [len(coin_types)]


# def remove_unused_coins(coin_types, amount):
#     for coin in coin_types:
#         if amount > coin:
#             coin_types.remove(coin)

#     return coin_types


# def making_change(amount, denominations):
#     if amount < 0:
#         "invalid amount given"
#     elif amount < 5:
#         return 1

#     h = 50  # half-dollar
#     q = 25  # quarter
#     d = 10  # dime
#     n = 5  # nickel
#     p = 1  # penny
#     coin_types = remove_unused_coins(denominations, amount)
#     coin_counts = [len(coin_types)]
#     change_combos = 0

#     def get_change_combo(coins, counts, start_i, total_amm):
#         pass

#     get_change_combo

#     pass

# def reverse_denominations(denominations):
#     new_denoms = []
#     for denom in reversed(denominations):
#         new_denoms.append(denom)

#     return new_denoms


# def making_change(amount, denominations):
#     if amount < 0:
#         "invalid amount given"
#     elif amount < 5:
#         return 1

#     coin_types = reverse_denominations(denominations)
#     print('coin_types = ' + str(coin_types))
#     coin_counts = [len(coin_types)]
#     num_of_combos = 0
#     index = 0

#     def get_change_combo(coins, counts, start_i, total_amm):
#         if start_i >= len(coins):
#             coin_combos = str(total_amm) + "="
#             for i in range(len(coins)):
#                 coin_combos += str(counts[i]) + "*" + str(coins[i] + "+")
#         print(coin_combos)

#         if start_i == len(coins):
#             if total_amm % coins[start_i] == 0:
#                 counts[start_i] = math.floor(total_amm / coins[start_i])
#                 get_change_combo(coins, counts, start_i+1, 0)
#         else:
#             for i in range(math.floor(total_amm / coins[start_i])):
#                 counts[start_i] = i
#                 get_change_combo(coins, counts, start_i+1,
#                                  total_amm-coins[start_i]*i)

#     get_change_combo(coin_types, coin_counts, index, amount)


def making_change(amount, coin_types):
    combos = [0 for amount in range(amount+1)]
    combos[0] = 1
    for d in coin_types:
        for amount in range(1, amount+1):
            if d <= amount:
                combos[amount] += combos[amount - d]
    return combos[amount]


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
