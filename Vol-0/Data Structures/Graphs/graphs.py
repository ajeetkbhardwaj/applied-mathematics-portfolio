"""
1. Graph Representations
   - Adjacency Matrix
   - Adjacency Lists
   - 
"""

# 1. Given a graph G = (V, E)
# 2. 

def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

def display_mat(mat):
    for row in mat:
        print(" ".join(map(str, row)))
# let's 
V = 4
mat = [[0] * V for _ in range(V)]
add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 3, 2)
add_edge(mat, 1, 3)
add_edge(mat, 2, 1)

print("Adjacency Matrix of G: \n")
display_mat(mat)

vertices = [1, 2, 3, 4]

import itertools
def complete_edges(vertices):
    edges=list(itertools.combinations(vertices,2))
    return edges
edges = complete_edges(vertices)
print("The graph G = (V, E)")
print(vertices, edges)


def add_edge(mat, edges):
    for i in range(4):
       for j in range(4):
          mat[i][j] = 1
          mat[j][i] = 1
V = 4
mat = [[0] * V for _ in range(V)]
add_edge(mat, edges)
display_mat(mat)

