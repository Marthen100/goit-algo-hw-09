import time

def find_coins_greedy(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    change = {}
    
    for coin in denominations:
        if amount == 0:
            break
        count = amount // coin
        if count > 0:
            change[coin] = count
        amount %= coin
        
    return change

def find_min_coins(amount):
    denominations = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in denominations:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin
    
    change = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        current_amount -= coin

    return change

def compare_methods(amount):
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Greedy method for {amount}: {greedy_result} with {sum(greedy_result.values())} coins. Time: {greedy_time:.6f} seconds.")
    print(f"Dynamic Programming method for {amount}: {dp_result} with {sum(dp_result.values())} coins. Time: {dp_time:.6f} seconds.")

# Example usage:
compare_methods(113)
compare_methods(132245)

