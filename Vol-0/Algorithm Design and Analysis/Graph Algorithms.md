---
marp: true
theme: gaia
class: invert
math: mathjx


---

# Graphs Algorithms

### Graph Traversal - visiting each components of a graph.

### 1. Breath First Search Algorithms
Breadth First Search (BFS) is an algorithm used for traversing or searching through graph and tree data structures. It explores all the neighbors of a node before moving on to the next level of nodes. 

1. Graph Representation: The graph is represented using an adjacency list (a dictionary where keys are nodes and values are lists of adjacent nodes).
2. Visited Set: A set is used to keep track of visited nodes to avoid cycles.
3. Queue: A double-ended queue (deque) from the collections module is used to efficiently manage the BFS traversal.
4. BFS Function: The bfs function processes each node by dequeuing it, printing it, and enqueuing all its unvisited neighbors.
```
procedure BFS(G, start)
    // Create a queue for BFS and a set to track visited nodes
    queue Q := empty queue
    mark start as visited
    Q.enqueue(start)

    while Q is not empty do
        // Dequeue a vertex from the queue
        v := Q.dequeue()
        // Process the current vertex (e.g., print it)
        print v

        // Get all adjacent vertices of the dequeued vertex v
        for each vertex u adjacent to v in G do
            if u is not visited then
                mark u as visited
                Q.enqueue(u)

// To handle the multiple components in  a disconnected graph
procedure init(G)
    for each vertex v in G do
        mark v as not visited

    for each vertex v in G do
        if v is not visited then
            BFS(G, v)
```
##### Depth First Search(DFS)


```
procedure DFS(G, v)
    // Mark the current node as visited
    mark v as visited
    // Process the current node (e.g., print it)
    print v

    // Recur for all the vertices adjacent to this vertex
    for each vertex u adjacent to v in G do
        if u is not visited then
            DFS(G, u)


procedure init(G)
    for each vertex v in G do
        mark v as not visited

    for each vertex v in G do
        if v is not visited then
            DFS(G, v)  // or DFS_iterative(G, v)
```

### Find strongly connected components in directed graphs

An Strongly connected component is a maximal subgraph where every pair of vertices is mutually reachable.

#### 1. Tarjan's Algorithm

Tarjan's algorithms uses depth-first search(DFS) to identify the strongly connected components in linear time. The key concepts is to maintain a stack of visited nodes and use indices and low-link values to track the components.

```
algorithm Tarjan(G)
    input: graph G = (V, E)
    output: set of strongly connected components (SCCs)

    index := 0
    S := empty stack
    for each v in V do
        if v.index is undefined then
            strongconnect(v)

function strongconnect(v)
    // Set the depth index for v to the smallest unused index
    v.index := index
    v.lowlink := index
    index := index + 1
    S.push(v)
    v.onStack := true

    // Consider successors of v
    for each (v, w) in E do
        if w.index is undefined then
            // Successor w has not yet been visited; recurse on it
            strongconnect(w)
            v.lowlink := min(v.lowlink, w.lowlink)
        else if w.onStack then
            // Successor w is in stack S and hence in the current SCC
            v.lowlink := min(v.lowlink, w.index)

    // If v is a root node, pop the stack and generate an SCC
    if v.lowlink = v.index then
        start a new strongly connected component
        repeat
            w := S.pop()
            w.onStack := false
            add w to current strongly connected component
        until w = v
      
        output the current strongly connected component
```
