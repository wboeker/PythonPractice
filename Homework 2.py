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

    def display(self):
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

# QUESTION TWO - display the tree above

# QUESTION THREE - search for the 2 values inside the tree, and 1 value without.

# QUESTION FOUR - count the number of even numbers in the tree above

# QUESTION FIVE - count the number of leaf nodes in the tree above



