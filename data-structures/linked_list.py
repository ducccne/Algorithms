"""
Linked List Data Structure
"""

class Node:
    """Node in a linked list."""
    
    def __init__(self, data):
        """
        Initialize a node.
        
        Args:
            data: Value to store in the node
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    Singly linked list implementation.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def is_empty(self):
        """Check if the linked list is empty."""
        return self.head is None
    
    def append(self, data):
        """
        Add a node at the end of the list.
        
        Args:
            data: Value to add
        """
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        """
        Add a node at the beginning of the list.
        
        Args:
            data: Value to add
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, data):
        """
        Delete the first occurrence of a value.
        
        Args:
            data: Value to delete
            
        Returns:
            True if deleted, False if not found
        """
        if self.is_empty():
            return False
        
        # If head node holds the data
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """
        Search for a value in the list.
        
        Args:
            data: Value to search for
            
        Returns:
            True if found, False otherwise
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def size(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        """String representation of the linked list."""
        if self.is_empty():
            return "LinkedList([])"
        
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return f"LinkedList([{' -> '.join(result)}])"


if __name__ == "__main__":
    # Example usage
    linked_list = LinkedList()
    
    print("Appending elements: 1, 2, 3")
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(f"List: {linked_list}")
    
    print("\nPrepending element: 0")
    linked_list.prepend(0)
    print(f"List: {linked_list}")
    
    print(f"\nSize: {linked_list.size()}")
    print(f"Search for 2: {linked_list.search(2)}")
    print(f"Search for 10: {linked_list.search(10)}")
    
    print("\nDeleting element: 2")
    linked_list.delete(2)
    print(f"List: {linked_list}")
