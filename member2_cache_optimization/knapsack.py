"""
0/1 Knapsack using Dynamic Programming
"""


def knapsack_01(values, weights, capacity):

    n = len(values)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]


    for i in range(1, n + 1):

        for w in range(capacity + 1):

            if weights[i - 1] <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] +
                    dp[i - 1][w - weights[i - 1]]
                )

            else:

                dp[i][w] = dp[i - 1][w]


    # Backtracking

    result = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            result.append(i - 1)
            w -= weights[i - 1]


    result.reverse()

    return result