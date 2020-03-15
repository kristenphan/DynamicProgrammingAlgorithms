# python3

from sys import stdin

# this function returns the maximum amount of gold that can be stuffed into a knapsack
# given a set of bold bards of various weights
# and a knapsack of a certain capacity
def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # create a 2D array to store the result of the amount of gold stuffed in the knapsack
    amount = [[float("inf")]*(capacity+1) for _ in range (len(weights)+1)]

    # if the capacity of the knapsack = 0, amount = 0
    for w in range(len(weights)+1):
        amount[w][0] = 0
    # if no gold bar is stuffed into the knapsack, amount = 0
    for c in range(capacity+1):
        amount[0][c] = 0
    # iterate through all gold bars and determine the maximum amount of gold that can be stuffed in the knapsack
    for w in range(1, len(weights)+1):
        for c in range(1, capacity+1):
            amount[w][c] = amount[w-1][c] # assume that gold bar of weight[w] does not get stuffed in the knapsack
            # now assume that there's enough room in the knapsack for this same gold bar,
            # calculate the value of the knapsack after adding this gold bar weights[w]
            if c >= weights[w-1]:
                value = amount[w-1][c-weights[w-1]] + weights[w-1]
                # if this value is greater than the current amount of gold in the knapsack,
                # update the amount of gold in the knapsack to include the gold bar
                if amount[w][c] < value:
                    amount[w][c] = value

    return amount[len(weights)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
