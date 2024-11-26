""" 

"""

# 1. Graph Traversal Algorithms
# 1.1 Depth First Search 
# 1.1.1 Recursive Implementation
def dfs_recursive(graph, v, visited):
    
    # Mark the current node as visited
    visited.add(v)
    print(v, end=' ')

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
def dfs_iterative(graph, start):
    # Create a stack for DFS and a set to track visited nodes
    stack = [start]
    visited = set()

    while stack:
        # Pop a vertex from the stack
        v = stack.pop()
        
        # Process the current vertex (e.g., print it)
        print(v, end=' ')
        
        # Push all unvisited adjacent vertices onto the stack
        for neighbor in graph.get(v, []):  # Use .get() to avoid KeyError
            if neighbor not in visited:
                visited.add(neighbor)  # Mark neighbor as visited
                stack.append(neighbor)  # Push neighbor onto the stack



def dfs_rec(graph, v):
    # Create a set to track visited vertices
    visited = set()

    # Perform DFS for each vertex to cover disconnected components
    for vertex in graph:
        if vertex not in visited:
            dfs_recursive(graph, vertex, visited)

def dfs_iter(graph, v):
    # Create a set to track visited vertices
    visited = set()

    # Perform DFS for each vertex to cover disconnected components
    for vertex in graph:
        if vertex not in visited:
           dfs_iterative(graph, v)

# Example usage:
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1, 4],
    4: [2],
    5: [6, 7, 8],
    6: [5, 8],
    7: [5, 7],
    8: [5, 6, 7]
}

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
print("DFS Recursive Traversal:")
#dfs_recursive(graph, 0, visited)
dfs_rec(graph, 'A')



# Example usage:
print("\nDFS Iterative Traversal:")
dfs_iter(graph, 'A')