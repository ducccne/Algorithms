"""
Quick Sort Algorithm
Time Complexity: O(n log n) average, O(n^2) worst case
Space Complexity: O(log n)
"""

def quick_sort(arr, low=0, high=None):
    """
    Sort an array using quick sort algorithm.
    
    Args:
        arr: List of comparable elements
        low: Starting index
        high: Ending index
        
    Returns:
        Sorted list
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition the array around a pivot element.
    
    Args:
        arr: List of comparable elements
        low: Starting index
        high: Ending index
        
    Returns:
        Pivot index
    """
    # Choose the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the pivot element with the element at i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    # Example usage
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    sorted_array = quick_sort(test_array.copy())
    print(f"Sorted array: {sorted_array}")
