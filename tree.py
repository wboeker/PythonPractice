# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
	def insertRight(self,newNode):
		if self.right == None:
			self.right = TreeNode(newNode)
		else:
			insertRight(self.right, newNode)
	def insertLeft (self,newNode):
		if self.left == None:
			self.left = TreeNode(newNode)
		else:
			insertLeft(self.left, newNode)

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

#Preorder traversal root left right
def preTraverse (node):
	if(node == None):
		return None
	print(node.val)
	preTraverse(node.left)
	preTraverse(node.right)

#Postorder traversal left right root
def postTraverse (node):
	if(node == None):
		return None
	postTraverse(node.left)
	postTraverse(node.right)
	print(node.val)
	
#call functions 
ioTraverse(BobJrTree)
print()
preTraverse(BobJrTree)
print()
postTraverse(BobJrTree)

#build big number tree

"""
numberTree = TreeNode(25)
insertRight(TreeNode,50)
insertRight(TreeNode,70)
insertRight(TreeNode,90)
insertLeft(TreeNode,15)
insertLeft(TreeNode,10)
insertLeft(TreeNode,4)
leftNum = TreeNode.left
rightNum = TreeNode.right
insertRight(leftNum,22)
insertRight(leftNum,24)
insertLeft(rightNum,35)
insertLeft(rightNum,31)
leftNum2 = leftNum.left
rightNum2 = rightNum.right
insertRight(leftNum2,12)
insertLeft(rightNum2,66)
leftRight = leftNum.right
rightLeft = rightNum.left
insertLeft(leftRight,18)
insertRight(rightLeft,44)

#repeat traversals
ioTraverse(numberTree)
print()
preTraverse(numberTree)
print()
postTraverse(numberTree)
"""
