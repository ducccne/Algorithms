"""
Stack Data Structure
LIFO (Last In First Out)
"""

class Stack:
    """
    Stack implementation using a list.
    """
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: Element to add
        """
        self.items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            Top element
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        """
        Return the top item without removing it.
        
        Returns:
            Top element
            
        Raises:
            IndexError: If stack is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
    
    def __str__(self):
        """String representation of the stack."""
        return f"Stack({self.items})"


if __name__ == "__main__":
    # Example usage
    stack = Stack()
    
    print("Pushing elements: 1, 2, 3, 4")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    
    print(f"Stack: {stack}")
    print(f"Size: {stack.size()}")
    print(f"Top element: {stack.peek()}")
    
    print(f"Popped: {stack.pop()}")
    print(f"Popped: {stack.pop()}")
    print(f"Stack after popping: {stack}")
