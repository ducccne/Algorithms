"""
Breadth-First Search (BFS) Algorithm
Time Complexity: O(V + E) where V is vertices and E is edges
Space Complexity: O(V)
"""

from collections import deque


def bfs(graph, start):
    """
    Perform breadth-first search traversal on a graph.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        
    Returns:
        List of vertices in BFS order
    """
    visited = set()
    queue = deque([start])
    result = []
    
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        # Visit all adjacent vertices
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def bfs_shortest_path(graph, start, goal):
    """
    Find shortest path between two vertices using BFS.
    
    Args:
        graph: Dictionary representing adjacency list
        start: Starting vertex
        goal: Target vertex
        
    Returns:
        List representing shortest path, or None if no path exists
    """
    if start == goal:
        return [start]
    
    visited = set([start])
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        vertex = path[-1]
        
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                
                if neighbor == goal:
                    return new_path
                
                visited.add(neighbor)
                queue.append(new_path)
    
    return None


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
    print("\nBFS traversal from 'A':", bfs(graph, 'A'))
    print("Shortest path from 'A' to 'F':", bfs_shortest_path(graph, 'A', 'F'))
