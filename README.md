Both functions solve the problem effectively, but the dynamic programming approach guarantees the optimal solution in terms of the minimum number of coins, whereas the greedy algorithm is generally faster but may not always yield the minimum coin count for every possible set of denominations.

Greedy Algorithm (find_coins_greedy): This method selects the largest denomination possible repeatedly until the amount is reduced to zero. It's fast and works well when the coin denominations are such that the larger denominations are multiples of the smaller ones

Dynamic Programming. This technique ensures that the minimum number of coins is used to make the change. It involves building up solutions to smaller sub-problems and using these solutions to solve the overall problem.
