
print("hello wendy :)")


# recursion!
# call function within a function!
# with every recursion problem
    # what's the base case!
    # how do we pass along our issuez

# factorialz!
def factorial(n):
    """
    calls n factorial - 1
    base case?
    n == 0??? return 1
    2! = 2 because 2 * 1 = 2
    3! = 6 because 3 * factorial(2)
    """
    if n == 0:
        return 1
    return n * factorial(n-1)


print("2 factorial is: " + str(factorial(2)))
print("4 factorial is: " + str(factorial(4)))
print("6 factorial is: " + str(factorial(6)))



class TreeNode:
    population = 0 

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        TreeNode.population += 1

    def searchBST(self, root, val):
        """
        if it's none, return none!
        called itself for the left
            left = FUNCTION CALL
        called itself for the right
            right = FUNCTION CALL
        if the node's value equals val,
            return that node! ^__^
        check left, right, and root
        """

        if root == None:
            return None

        if root.val == val:
            return root
        

        left = self.searchBST(root.left, val)
        right = self.searchBST(root.right, val)
        
        if left != None:
            if left.val == val:
                return left

        if right != None:
            if right.val == val:
                return right

        return None



# print("treenode val" + str(TreeNode.val)) # this is gonna error

# bobz
print("old pop: " + str(TreeNode.population))
BobJrTree = TreeNode("Alice")
left = TreeNode("Bob")
right = TreeNode("Carol") # CAROL
left2 = TreeNode("Bob Jr.")
print("new pop: " + str(TreeNode.population))

BobJrTree.left = left
BobJrTree.right = right
left.left = left2

print("pop: " + str(BobJrTree.population))
print("val: " + str(BobJrTree.val))


print("===================")

BobJrTree.searchBST(BobJrTree, "Carol")

assert(1 == 1)

hopefullyCarolTree = BobJrTree.searchBST(BobJrTree, "Carol")
assert(hopefullyCarolTree.val == right.val)
hopefullyBobJrTree = BobJrTree.searchBST(BobJrTree, "Bob Jr.")
assert(hopefullyBobJrTree.val == left2.val)



