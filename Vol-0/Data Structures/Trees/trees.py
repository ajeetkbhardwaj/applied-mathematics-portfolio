""" 

"""
#%%
# 1. represent Nodes in tree
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []



#%%
# 3. Tree Traversal : visiting each nodes of tree exactly once in certain order.
"""
1. Depth First Search or DFS
   - Inorder Traversal
   - Preorder Traversal
   - Postorder Traversal
2. Level Order Traversal(Breadth First Search) BFS

Function Inorder(tree) 
  Traverse the left subtree, i.e., call Inorder(left->subtree) 
  Visit the root. 
  Traverse the right subtree, i.e., call Inorder(right->subtree) 

Function  Preorder(tree) 
  Visit the root. 
  Traverse the left subtree, i.e., call Preorder(left->subtree) 
  Traverse the right subtree, i.e., call Preorder(right->subtree) 

Function 


Function LevelOrder(tree) 
   Create an empty queue Q 
   Enqueue the root node of the tree to Q 
   Loop while Q is not empty 
      Dequeue a node from Q and visit it 
      Enqueue the left child of the dequeued node if it exists 
      Enqueue the right child of the dequeued node if it exists

      
Function BoundaryTraversal(tree) 
 If root is not null: 
     Print root’s data 
     PrintLeftBoundary(root->left) // Print the left boundary nodes 
     PrintLeafNodes(root->left) // Print the leaf nodes of left subtree 
     PrintLeafNodes(root->right) // Print the leaf nodes of right subtree 
     PrintRightBoundary(root->right) // Print the right boundary nodes     
      
Function  DiagonalTraversal(tree): 
 If root is not null: 
    Create an empty map 
    DiagonalTraversalUtil(root, 0, M) // Call helper function with initial diagonal level 0 
    For each key-value pair (diagonalLevel, nodes) in M: 
       For each node in nodes: 
       Print node’s data   

Function  DiagonalTraversalUtil(node, diagonalLevel, M): 
 If node is null: 
 Return 
 If diagonalLevel is not present in M: 
    Create a new list in M for diagonalLevel 
 Append node’s data to the list at M[diagonalLevel] 
 DiagonalTraversalUtil(node->left, diagonalLevel + 1, M) // Traverse left child with increased diagonal level 
 DiagonalTraversalUtil(node->right, diagonalLevel, M) // Traverse right child with same diagonal level     
      
"""
from collections import deque
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def InorderTraversal(root):
    # base case  if null
    if root is None:
        return
    
    # recursion on left subtree
    InorderTraversal(root.left)
    # visiting the current node
    print(root.data, end = " ")
    # recursion on the right subtree
    InorderTraversal(root.right)
def PostorderTraversal(root):
    # base case  if null
    if root is None:
        return
    
    # recursion on left subtree
    PostorderTraversal(root.left)
   
    # recursion on the right subtree
    PostorderTraversal(root.right)

     # visiting the current node
    print(root.data, end = " ")

def PreorderTraversal(root):
    # base case  if null
    if root is None:
        return
    # visiting the current node
    print(root.data, end = " ")
    # recursion on left subtree
    PreorderTraversal(root.left)
    # recursion on the right subtree
    PreorderTraversal(root.right)

def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def boundary_traversal(root):
    if root is None:
        return
    
    if root is not None:
        print(root.data, end= " ")
        print(root.left)
        print(root.left)
        print()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
InorderTraversal(root)
PreorderTraversal(root)
PostorderTraversal(root)
print(level_order_traversal(root))
# %%
