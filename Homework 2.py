# Homework 2
# 45-60 min

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
		"""
		QUESTION TWO(d)
		write a function that prints out the tree how you choose
		will be called with 
		my_tree.display()
		"""
		if(node == None):
		return None
		ioTraverse(node.left)
		print(node.val)
		ioTraverse(node.right)

	def searchBST(self, root, val):
		"""
		QUESTION THREE(d)
		implement searchBST
		will be called with my_tree.searchBST(my_tree, 406)
		returns the subtree or None
		"""
		pass

	def countEvenNumbers(self, root, val):
		"""
		QUESTION FOUR(d)
		recursively count the number of even numbers that appear in the tree
		returns an integer
		"""
		pass

	def countLeafNodes(self, root, val):
		"""
		QUESTION FIVE
		count the total number of "leaf nodes" aka Kidless nodes
		returns an integer
		"""
		pass


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

# QUESTION TWO - display the tree above
display(numberTree)

# QUESTION THREE - search for the 2 values inside the tree, and 1 value without.

# QUESTION FOUR - count the number of even numbers in the tree above

# QUESTION FIVE - count the number of leaf nodes in the tree above

# ... replace the pass with your own code

