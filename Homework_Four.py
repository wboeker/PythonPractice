# Homework 4
# less 60 min

def syllables_indices(s, indices):
	"""
	QUESTION 1
		write a function that prints out 3 letter chunks of the above string for each index in the above array

		s = ['wendeebayker']
		indices = [0, 0, 3, 0, 0, 3, 0, 0, 3, 6, 3, 0]
		syllables(s, indices)
		wen
		wen
		dee
		wen
		... etc.
		use [::] in your answer friend :)

	"""
	pass


def find_pairs(words_dict):
	"""
	QUESTION 2
		write a function that will print each key and value in the dictionary
		
		for the dictionary {'a': 1, 'b': 2, 'c': 3}

		print
		>>> a maps to 1
		>>> b maps to 2
		>>> c maps to 3
		
	"""
	pass


def secret_code(code, message):
	"""
	QUESTION 3
		write a function that decodes the message
		the message is an array of strings
		the code is a dictionary mapping <codeword>: real word
		if the word does not appear in the code, leave it alone
		
		code = {
			"mango": "hug",
			"tea": "now",
			"mr.": "bear",
			"bear: "cal"
		}
		message = ["I", "want", "to", "mango", "my", "bear", "mr.", "tea"]
		>>> I want to hug my cal bear now

	"""
	pass
	

def count_unique_words(s):
	"""
	QUESTION 4
		find the number of unique words in the string
		words are delimited by the " " key
		"word."" is different than "word"

		s = "This is a string with a lot of strings."
		>>> 8
	"""
	pass

def count_letters(s):
	"""
	QUESTION 5
		return a letter dictionary where
			the keys are the letters in the string s
			the values are the number of times that letters appear
		s = "i am a lazy egg"
		>>> {'a': 3, "i", 1, "m": 1, "l": 1, "z": 1, "e": 1, "y": 1, "g": 2}
	"""
	pass
