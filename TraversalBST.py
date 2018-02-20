#1. Preorder
#2. Inorder
#3. Postorder
#4. Breadth First / Level Order Traversal

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
