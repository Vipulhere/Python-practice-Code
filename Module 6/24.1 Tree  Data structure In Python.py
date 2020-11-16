from binarytree import Node
from binarytree import build

root=Node(3)
root.left=Node(5)
root.right=Node(9)
root.right=Node(4)

print("Binary Tree",root)
print("list",list(root))
print("inorder of nodes",root.inorder)
print("size of tree",root.size)
print("height of tree",root.height)
print("________________")

nodes={1,2,4,5,6,8,9,77}
birany=build(nodes)
print("binary tree :\n",birany)
print("\n list of binary tree",birany.values)
print("list",list(birany))
print("inorder of nodes",birany.inorder)
print("size of tree",birany.size)
print("height of tree",birany.height)