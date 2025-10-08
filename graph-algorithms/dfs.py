"""
Depth-First Search (DFS) Algorithm
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)
"""


def dfs_recursive(graph, vertex, visited=None):
    """
    Perform depth-first search traversal recursively.
    
    Args:
        graph: Dictionary representing adjacency list
        vertex: Current vertex
        visited: Set of visited vertices
        
    Returns:
        List of vertices in DFS order
    """
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    result = [vertex]
    
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    
    return result


def dfs_iterative(graph, start):
    """
    Perform depth-first search traversal iteratively.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        
    Returns:
        List of vertices in DFS order
    """
    visited = set()
    stack = [start]
    result = []
    
    while stack:
        vertex = stack.pop()
        
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            
            # Add neighbors to stack (reverse order for left-to-right traversal)
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return result


if __name__ == "__main__":
    # Example graph (adjacency list)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Graph:", graph)
    print("\nDFS traversal (recursive) from 'A':", dfs_recursive(graph, 'A'))
    print("DFS traversal (iterative) from 'A':", dfs_iterative(graph, 'A'))
