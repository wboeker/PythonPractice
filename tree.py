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
			self.right.insertRight(newNode)
	def insertLeft (self,newNode):
		if self.left == None:
			self.left = TreeNode(newNode)
		else:
			self.left.insertLeft(newNode)

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


numberTree = TreeNode(25)
numberTree.insertRight(50)
numberTree.insertRight(70)
numberTree.insertRight(90)
numberTree.insertLeft(15)
numberTree.insertLeft(10)
numberTree.insertLeft(4)
leftNum = numberTree.left
rightNum = numberTree.right
leftNum.insertRight(22)
leftNum.insertRight(24)
rightNum.insertLeft(35)
rightNum.insertLeft(31)
leftNum2 = leftNum.left
rightNum2 = rightNum.right
leftNum2.insertRight(12)
rightNum2.insertLeft(66)
leftRight = leftNum.right
rightLeft = rightNum.left
leftRight.insertLeft(18)
rightLeft.insertRight(44)

#repeat traversals
ioTraverse(numberTree)
print()
preTraverse(numberTree)
print()
postTraverse(numberTree)

