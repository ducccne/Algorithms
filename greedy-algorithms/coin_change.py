"""
Coin Change Problem using Greedy Algorithm
Note: Greedy approach doesn't always give optimal solution for all coin systems
Time Complexity: O(n) where n is the number of coin denominations
Space Complexity: O(1)
"""


def coin_change_greedy(coins, amount):
    """
    Find minimum number of coins needed using greedy approach.
    Works optimally for canonical coin systems (like US coins).
    
    Args:
        coins: List of coin denominations (must be sorted in descending order)
        amount: Target amount
        
    Returns:
        Dictionary with coin denominations and their counts, or None if not possible
    """
    result = {}
    remaining = amount
    
    for coin in coins:
        if remaining >= coin:
            count = remaining // coin
            result[coin] = count
            remaining -= coin * count
    
    if remaining > 0:
        return None  # Cannot make exact change
    
    return result


def coin_change_greedy_count(coins, amount):
    """
    Find minimum number of coins needed (returns count only).
    
    Args:
        coins: List of coin denominations (must be sorted in descending order)
        amount: Target amount
        
    Returns:
        Minimum number of coins, or -1 if not possible
    """
    count = 0
    remaining = amount
    
    for coin in coins:
        if remaining >= coin:
            count += remaining // coin
            remaining %= coin
    
    return count if remaining == 0 else -1


if __name__ == "__main__":
    # US coin system (works optimally with greedy)
    coins = [25, 10, 5, 1]  # quarters, dimes, nickels, pennies
    amount = 67
    
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    
    result = coin_change_greedy(coins, amount)
    print(f"\nCoins needed: {result}")
    
    if result:
        total_coins = sum(result.values())
        print(f"Total number of coins: {total_coins}")
        
        # Display the breakdown
        for coin, count in sorted(result.items(), reverse=True):
            print(f"  {count} x {coin}¢")
    
    # Alternative: just get the count
    count = coin_change_greedy_count(coins, amount)
    print(f"\nMinimum coins needed: {count}")
