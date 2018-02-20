    1
   / \
  2   3
 / \
4   5

#1. Preorder (root, left, right):  1 2 4 5 3
#2. Inorder (left, root, right):   4 2 5 1 3
#3. Postorder (left, right, root): 4 5 2 3 1
#4. Breadth First / Level Order Traversal (root): 1 2 3 4 5

#1. Preorder with input argument tree
def preorder(tree):
  if tree:
    print(tree.getRootVal())
    preorder(tree.getLeftChild())
    preorder(tree.getRightChild())
    

#1. Preorder with input argument node
def preorder(self):
  print(self.key)
  if self.leftChild:
    self.leftChild.preorder()
  if self.leftRight:
    self.rightChild.preorder()
    
#2. Inorder
def inorder(tree):
  if tree:
    inorder(tree.getLeftChild())
    print(tree.getRootVal())
    inorder(tree.getRightChild())
    
    
#3. Postorder
def postorder(tree):
  if tree:
    postorder(tree.getLeftChild())
    postorder(tree.getRightChild())
    print(tree.getRootVal())
