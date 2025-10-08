"""
Binary Search Algorithm
Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive
"""

def binary_search_iterative(arr, target):
    """
    Search for a target element using iterative binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Search for a target element using recursive binary search.
    
    Args:
        arr: Sorted list of comparable elements
        target: Element to search for
        left: Left boundary index
        right: Right boundary index
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    # Example usage
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7
    
    print(f"Array: {test_array}")
    print(f"Target: {target}")
    
    index_iterative = binary_search_iterative(test_array, target)
    print(f"Iterative search - Index: {index_iterative}")
    
    index_recursive = binary_search_recursive(test_array, target)
    print(f"Recursive search - Index: {index_recursive}")
