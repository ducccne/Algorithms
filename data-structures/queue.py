"""
Queue Data Structure
FIFO (First In First Out)
"""

class Queue:
    """
    Queue implementation using a list.
    """
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """
        Add an item to the rear of the queue.
        
        Args:
            item: Element to add
        """
        self.items.append(item)
    
    def dequeue(self):
        """
        Remove and return the front item from the queue.
        
        Returns:
            Front element
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """
        Return the front item without removing it.
        
        Returns:
            Front element
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)
    
    def __str__(self):
        """String representation of the queue."""
        return f"Queue({self.items})"


if __name__ == "__main__":
    # Example usage
    queue = Queue()
    
    print("Enqueuing elements: 1, 2, 3, 4")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    print(f"Queue: {queue}")
    print(f"Size: {queue.size()}")
    print(f"Front element: {queue.front()}")
    
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue after dequeuing: {queue}")
