# Homework 6
# 60-90 min

class TreeNode:

    def __init__(self, x):
    	"""
		QUESTION ONE at the bottom :)

		NOTE: this is not a binary tree anymore. children can be any size
    	"""
        self.val = x
        self.children = []

    def __str__(self):
    	"""
		calling str(myTreeNode) will call this function
		feel free to change this if you want.
    	"""
    	return '(' + str(self.val) + ': ' + str(self.children) + ')'

    def layer_display(self):
    	"""
		QUESTION TWO(d)
		write a function that prints out the tree
		will be called with 
		my_tree.layer_display()

		This time, display the tree by layer with values separated by spaces

		for the tree:

			6
		  3   7
		 145  8
 
 		print:

 		6
 		3 7
 		1 4 5 8 
    	"""
    	pass

    def search_tree(self, val):
    	"""
		QUESTION THREE(d)
		implement searchBST
		will be called with my_tree.searchBST(406)
		returns the subtree or None
    	"""
    	pass

    def count_even_numbers(self, val):
    	"""
		QUESTION FOUR(d)
		recursively count the number of even numbers that appear in the tree
		returns an integer

		for the the tree defined in 'layer_display' - the solution is 3
    	"""
    	pass

    def print_path(self, val):
    	"""
		QUESTION FIVE
		
		this is another stretch one we'll go over if you can't figure it out.

		Your goal is to find the val in the tree, and also print the path leading up to the val

				 8
			5		 9
		  1 6 7           12
		  0           10      18
		              11   15 19 21

		and the tree is the root, searching for 11:
			return [8, 9, 12, 10, 11]

		bnut searching for 13
			return None
    	"""
    	pass