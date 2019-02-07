# Homework 2
# 45-60 min

import pdb

class TreeNode:
	population = 0 

	def __init__(self, x):
		"""
		QUESTION ONE at the bottom :)
		"""
		self.val = x
		self.left = None
		self.right = None
		TreeNode.population += 1

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

	def display(self):
		if self is None:
			return None
		if self.left != None:
			self.left.display()
		print(self.val)
		if self.right != None:
			self.right.display()
		"""
		QUESTION TWO(d)
		write a function that prints out the tree how you choose
		will be called with 
		my_tree.display()
		"""

	def searchBST(self, root, val):
		"""
		QUESTION THREE(d)
		implement searchBST
		will be called with my_tree.searchBST(my_tree, 406)
		returns the subtree or None
		"""
		if root is None:
			return None
		if root.val == val:
			return root
		#searches the left and right
		left = self.searchBST(root.left,val)
		right = self.searchBST(root.right,val)
		if left and left.val == val:
			return left
		if right and right.val == val:
			return right
		else:
			return None

	def countEvenNumbers(self, root):
		"""
		QUESTION FOUR(d)
		recursively count the number of even numbers that appear in the tree
		returns an integer
		"""
		if root is None:
			return 0

		leftCount = 0
		rightCount = 0

		if root.left != None:
			leftCount = self.countEvenNumbers(root.left)

		if root.right != None:
			rightCount = self.countEvenNumbers(root.right)

		if root and root.val %2 == 0:
		 	return leftCount + rightCount + 1
		else:
		 	return leftCount + rightCount

	def countLeafNodes(self, root):
		"""
		QUESTION FIVE
		count the total number of "leaf nodes" aka Kidless nodes
		returns an integer
		"""
		if root is None:
			return 0

		if root.left is None and root.right is None:
			return 1

		leftLeaves = 0
		rightLeaves = 0

		if root.left != None:
			leftLeaves = self.countLeafNodes(root.left)
		if root.right != None:
			rightLeaves = self.countLeafNodes(root.right)

		return leftLeaves + rightLeaves


# QUESTION ONE - Create a large tree of integers (at least 8 nodes)

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

BobJrTree = TreeNode("Alice")
left = TreeNode("Bob")
right = TreeNode("Carol")
left2 = TreeNode("Bob Jr.")
BobJrTree.left = left
BobJrTree.right = right
left.left = left2

# QUESTION TWO - display the tree above
numberTree.display()

# QUESTION THREE - search for the 2 values inside the tree, and 1 value without.

fourTree = numberTree.searchBST(numberTree,4)
tenTree = numberTree.searchBST(numberTree,10)
noTree = numberTree.searchBST(numberTree,100)
print("fourTree: ", fourTree.val)
print("tenTree: ", tenTree.val)
print("noTree: ", noTree)

# QUESTION FOUR - count the number of even numbers in the tree above
print("Number of Even Numbers: ", numberTree.countEvenNumbers(numberTree))
# QUESTION FIVE - count the number of leaf nodes in the tree above

# ... replace the pass with your own code
print("Number of leafless Nodes: ", BobJrTree.countLeafNodes(BobJrTree))

