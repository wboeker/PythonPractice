# Homework 3
# 45-60 min

def reverse(s):
		reverseStr = ""
		for letter in s:
			reverseStr = letter + reverseStr
		return reverseStr

def line_by_line(s):
	"""
	QUESTION 1
		write a function that prints out each letter of the word on a separate line and then
		prints out the same word backwards

		line_by_line('mango')
		m
		a
		n
		g
		o
		o
		g
		n
		a
		m
	"""

	for letter in s:
		print(letter)
	for letter in reverse(s):
		print(letter)

def one_two_one(s):
	"""
	QUESTION 2
		write a function that will print a string s in the following pattern
		1
		121
		12321
		1234321
			... for the string '1234'
	"""

	for i in range(len(s)):
		shortStr = s[0:i + 1]
		print(shortStr,reverse(shortStr)[1:len(shortStr)], sep='')

	# print(s[0])
	# print(s[0:2],s[0])
	# print(s[0:3],s[1],s[0])
	# print(s[0:4],s[2],s[1],s[0])

def is_palindrome(s):
	"""
	QUESTION 3
		write a function that returns a boolean whether the string is a palindrome
		will be called with 
		is_palindrome("racecar")
		assume no spaces
	"""
	reverse(s)
	if s == reverse(s):
		return True
	else:
		return False
	

def is_palindrome_with_spaces(s):
	"""
	QUESTION 4
		same as above but the string can have spaces
		spaces should be ignored
		is_palindrome_with_spaces(" madam im adam         ")
	"""
	#remove whitespace
	s = ''.join(s.split())

	return is_palindrome(s)

def find_palindrome_pivot(s):
	"""
	QUESTION 5
		find the index where the palindrome begins to wrap
		return the first index if there are two
		find_palindrome_pivot(" madam im adam         ")
			>>> returns 7 because the 'i' is index 7 of the string
		find_palindrome_pivot("racecar")
			>>> 3
		find_palindrome_pivot("lollol")
			>>> 2 - because it's 2 and 3 that are the pivots.
	"""
	#initialize index
	index = 0

	#remove whitespace
	noWhitespace = ''.join(s.split())

	if s == noWhitespace:
		#if length is even, divide length in 2 and subtract 1, else divide by 2
		if len(noWhitespace) %2 == 0:
			index = int(len(noWhitespace)/2) - 1
		else:
			index = int(len(noWhitespace)/2)
	else:
		#count number of spaces in s
		spaceCount = 0
		index += spaceCount

	return index
	
line_by_line("mango")
one_two_one("1234")
print(is_palindrome("racecars"))
print(is_palindrome_with_spaces("race car"))
print(find_palindrome_pivot("lollol"))