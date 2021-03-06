# Homework 5
# 60-90

def climb_stairs(num_steps, step_size):
	"""
	QUESTION ONE 
		mr. climber needs to climb 'num_steps' steps. the boy/man uses step_size of stepsize to climb.
		he takes an extra step to finish when rounding

		climb_stairs(17, 1) ==> 17
		climb_stairs(18, 4) ==> 5 (4 steps to get to the 16th step, then one more)
	"""

	steps_taken = num_steps//step_size 
	if num_steps % step_size != 0:
		steps_taken += 1
	return steps_taken

def build_mountain(num):
	num_list = []
	for i in range(1,num):
		num_list.append(i)
	length = len(num_list)
	for j in range(num):
		num_list.append(num-j)
	return num_list

def climb_one_two_one(num_steps):
	"""
	QUESTION TWO 
		mr. climber has a friend named Won Tuhuan. Won always takes steps in the following pattern
			1
			121
			12321
			1234321
			... etc

		find the number of steps Mr. Tuhuan takes to climb.

		climb_one_two_one(20)
			1: his first step gets him to step 1

			1: his second step gets him to step 2 
			2: his third step gets him to step 4
			1: his fourth step gets him to step 5

			1: 5th step ==> 6
			2: 6th step ==> 8
			3: 7th step ==> 11
			2: 8th step ==> 13
			1: 9th step ==> 14

			1: 10th step ==> 15
			2: 11th step ==> 17
			3: 12th step ==> 20

			the answer is 12.
	"""
	num_list = []
	num_strides = 0
	steps_taken = 0
	for i in range(num_steps+1):
		num_list = num_list + build_mountain(i)
	print(num_list)
	for x in num_list:
		steps_taken += x
		num_strides += 1
		if steps_taken >= num_steps:
			break
	return num_strides


def climb_with_plan(num_steps, plan):
	"""
	QUESTION THREE
		"Always make plan!" - Confucius probably

		Plan R. always makes plan ahead of time! Otherwise lazy! 
		Plan R. make plan ahead of time, then follows plan. Unlike Mr. Climber and Won Tuhuan. They always lazy.

		plan is a list of steps
		return None when the plan was bu hao - and not far enough.

		climb_with_plan(19, [4, 6, 4, 1, 2, 9, 0, 0, 0, 0, 0, 100])
			>>> 6
			>>> because after finishing the 6th step (9), we pass 19.
		
		climb_with_plan(19, [-5, 5, -5, 5, -5, 5, -5, 5])
			>>> None
			>>> bad plan!
	"""
	steps_taken = 0
	num_strides = 0
	for x in plan:
		steps_taken += x
		num_strides += 1
		if steps_taken >= num_steps:
			return num_strides
			break
	if steps_taken < num_steps:
		return None


def climb_one_or_two(num_steps, holes):
	"""
	QUESTION FOUR
		Smart Tea is a smartie and can decide to use two steps or one step.
		but the Diggin Holes company has dug holes in the staircase!
		Holez are bad. Smart Tea cannot step on a holy step.

		Smart Tea starts on "step 0"

		holes = [2, 5]
		num_steps = 10
		climb_one_or_two(num_steps, holes)

		smart tea does the following
		1) take a single step landing on step 1. 
			She cannot take a double b/c of the hole
		2) take a double step landing on step 3.
			she skips the dug hole in her way!
		3) take a single step landing on step 4.
			there's a hole ahead!
		4) take a double step landing on step 6.
		5) double step to step 8
		6) double step to step 10

		6 steps!
		HINT: use recursion or iterative methodz up to you!
	"""
	"""
	num_list = []
	num_strides = 0
	steps_taken = 0
	bBoolean = True
	for i in range(1,num_steps+1):
		bBoolean = True
		for x in holes:
			if x == i:
				bBoolean = False
		if bBoolean:
			num_list.append(i)
	print(num_list)
	for i in range(len(num_list)-1):
		if steps_taken >= num_steps:
			break;
		if num_list[i+1] == num_list[i]+1:
			steps_taken += 2
			num_strides += 1
		else:
			steps_taken += 1
			num_strides += 1
	return num_strides
	"""
	new_array = [num_steps-x for x in holes]
	new_set = set(new_array)
	def helper(k):
		if k in new_set:
			return float("inf")
		if k <= 0:
			return 0
		else:
			return 1 + min(helper(k-1), helper(k-2))
	return helper(num_steps)

def climb_one_or_two_or_three(num_steps, holes):
	"""
	Smarter T. is going by the same rules as before, but can take
		1
		2
		or 3 steps per move!
	
	holes = [2, 5]
	num_steps = 10
	climb_one_or_two_or_three(num_steps, holes)
	1) land on step 3
	2) land on step 6
	3) land on step 9
	4) finish

	return 4


	holes = [3, 6]
	num_steps = 10
	climb_one_or_two_or_three(num_steps, holes)

	1) take a double-step to land on 2
	2) take a triple-step to land on 5
	3) take a triple-step on land on 8
	4) finish

	return 4


	don't spend forever i will feel bad :(
	"""
	#building list without holes
	num_list = []
	num_strides = 0
	steps_taken = 0
	bBoolean = True
	for i in range(1,num_steps+1):
		bBoolean = True
		for x in holes:
			if x == i:
				bBoolean = False
		if bBoolean:
			num_list.append(i)

	#counting steps
	for i in range(len(num_list)-1):
		if steps_taken >= num_steps:
			break;
		if num_list[i+1] == num_list[i]+2:
			steps_taken += 3
		elif num_list[i+1] == num_list[i]+1:
			steps_taken += 2
		else:
			steps_taken += 1
		num_strides +=1
	return num_strides

holes = [2,5,7,9]
num_steps = 10
print(climb_one_or_two(num_steps, holes))
