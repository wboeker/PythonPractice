# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#build Bob Jr Tree from Slides in code and print out
#traverse tree in 3 ways and print out traversals
#repeat for big number tree
#traverse in each of the three ways

BobJrTree = TreeNode("Alice")
left = TreeNode("Bob")
right = TreeNode("Carol")
left2 = TreeNode("Bob Jr.")
BobJrTree.left = left
BobJrTree.right = right
left.left = left2

#in order traversal left me right
def ioTraverse (node):
	if(node == None):
		return None
	ioTraverse(node.left)
	print(node.val)
	ioTraverse(node.right)
	
#call function ioTraverse
ioTraverse(BobJrTree)
