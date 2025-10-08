"""
Linear Search Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    """
    Search for a target element using linear search.
    
    Args:
        arr: List of comparable elements
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Find all occurrences of a target element using linear search.
    
    Args:
        arr: List of comparable elements
        target: Element to search for
        
    Returns:
        List of indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


if __name__ == "__main__":
    # Example usage
    test_array = [64, 34, 25, 12, 22, 11, 90, 22]
    target = 22
    
    print(f"Array: {test_array}")
    print(f"Target: {target}")
    
    index = linear_search(test_array, target)
    print(f"First occurrence at index: {index}")
    
    all_indices = linear_search_all(test_array, target)
    print(f"All occurrences at indices: {all_indices}")
