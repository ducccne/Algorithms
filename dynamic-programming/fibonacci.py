"""
Fibonacci Number Calculation
Different approaches with varying time and space complexity
"""


def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion.
    Time Complexity: O(2^n)
    Space Complexity: O(n)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    Calculate nth Fibonacci number using memoization.
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Position in Fibonacci sequence
        memo: Dictionary to store computed values
        
    Returns:
        nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n):
    """
    Calculate nth Fibonacci number using tabulation (bottom-up).
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    # Create table to store Fibonacci numbers
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_optimized(n):
    """
    Calculate nth Fibonacci number using space-optimized approach.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    prev2 = 0
    prev1 = 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci number at position {n}:")
    print(f"Recursive: {fibonacci_recursive(n)}")
    print(f"Memoization: {fibonacci_memoization(n)}")
    print(f"Tabulation: {fibonacci_tabulation(n)}")
    print(f"Optimized: {fibonacci_optimized(n)}")
    
    # For larger n, only use optimized approaches
    n = 30
    print(f"\nFibonacci number at position {n}:")
    print(f"Memoization: {fibonacci_memoization(n)}")
    print(f"Tabulation: {fibonacci_tabulation(n)}")
    print(f"Optimized: {fibonacci_optimized(n)}")
