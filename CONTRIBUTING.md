# Contributing Guidelines

Thank you for your interest in this algorithms repository!

## Purpose

This repository is a personal learning collection for algorithm implementations. It serves as a reference while learning computer science fundamentals.

## Adding New Algorithms

When adding new algorithm implementations, please follow these guidelines:

### 1. File Structure
- Place the algorithm in the appropriate category directory
- If a new category is needed, create a new directory with a README.md

### 2. Code Style
- Use clear, descriptive variable names
- Include docstrings for functions and classes
- Add comments for complex logic
- Follow PEP 8 style guide for Python code

### 3. Documentation
Each algorithm file should include:
- A module docstring explaining the algorithm
- Time and space complexity analysis
- Clear function docstrings with parameters and return values
- Example usage in `if __name__ == "__main__"` block

### 4. Example Template

```python
"""
Algorithm Name
Time Complexity: O(?)
Space Complexity: O(?)
"""

def algorithm_function(params):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation here
    pass


if __name__ == "__main__":
    # Example usage
    print("Example output")
```

### 5. Testing
- Test your implementation before committing
- Include diverse test cases in the example usage
- Verify edge cases are handled

## Categories

Current categories include:
- `sorting/` - Sorting algorithms
- `searching/` - Searching algorithms
- `data-structures/` - Data structure implementations
- `graph-algorithms/` - Graph traversal and pathfinding
- `dynamic-programming/` - Dynamic programming solutions
- `greedy-algorithms/` - Greedy algorithm approaches

Feel free to suggest new categories if needed!

## Questions?

This is a learning repository, so feel free to experiment and learn!
