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
	for index in indices:
		print(s[index:index+3])

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
	for key,value in words_dict.items():
		print(key + " maps to " + str(value))

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
	for word in enumerate(message, start=1):
		for key,value in code.items():
			if word == key:
				message = value
	return message

def count_unique_words(s):
	"""
	QUESTION 4
		find the number of unique words in the string
		words are delimited by the " " key
		"word."" is different than "word"

		s = "This is a string with a lot of strings."
		>>> 8
	"""
	words = s.split()
	uniqueHash = {}
	for word in words:
		if word in uniqueHash:
			uniqueHash[word] += 1
		else:
			uniqueHash[word] = 1

	return len(uniqueHash)

def count_letters(s):
	"""
	QUESTION 5
		return a letter dictionary where
			the keys are the letters in the string s
			the values are the number of times that letters appear
		s = "i am a lazy egg"
		>>> {'a': 3, "i", 1, "m": 1, "l": 1, "z": 1, "e": 1, "y": 1, "g": 2}
	"""
	uniqueHash = {}
	for letter in s:
		if letter != ' ':
			if letter in uniqueHash:
				uniqueHash[letter] += 1
			else:
				uniqueHash[letter] = 1

	return uniqueHash


testArray = [0, 0, 3, 6]
syllables_indices("wendeebayker", testArray)
testDict = {}
testDict["a"] = 1
testDict["b"] = 2
testDict["c"] = 3
find_pairs(testDict)

code = {
	"mango": "hug",
	"tea": "now",
	"mr.": "bear",
	"bear": "cal"
	}

message = ["I", "want", "to", "mango", "my", "bear", "mr.", "tea"]

print(secret_code(code, message))

print(count_unique_words("This is a string with a lot of strings."))
print(count_letters("i am a lazy egg"))

