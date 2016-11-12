"""
Copyright (c) Jia Rong Wu 2016
bmh.py is an implementation for the Boyer-Moore-Horspool algorithm
"""

def match_table(pattern):
	""" 
	Preprocessing step for the BMH algorithm
	Handles matches with strings containing ASCII characters 0-127
	Uses the python dictionary structure to store the match table
	@pattern is the pattern being searched
	@return the match_table for pattern
	"""

	skip_table = {}

	# Build a skip table for the range of valid ASCII characters
	# Set initial value for the skip table to be the length of the pattern to be matched
	# Adjust s and e as desired to change range of characters permitted

	s = 0
	e = 256

	try:
		# Initialize all distances in the skip table to the pattern length
		for i in range(s,e):
			skip_table[chr(i)] = len(pattern)
		# Decrement each occurence of the character in the pattern by M-i-1
		for i in range(0,len(pattern)-1):
			skip_table[pattern[i]] = len(pattern) - i - 1

		return skip_table

	except ValueError:
		pass

def match_search(pattern, target):
	"""
	match_search takes a target string and searches for the substring pattern
	Only returns the first occurrence of pattern.
	@param pattern is the pattern to be found
	@param target is the string to search in
	@return the index in target where pattern is first located if located
	@return -1 if no pattern is found
	"""

	# Define the skip table for the pattern to be matched
	skip_table = match_table(pattern)

	skip = 0

	# While the search window is less than the length of the pattern to match
	while (len(target) - skip >= len(pattern)):

		# Start comparing at last character of pattern
		i = len(pattern) - 1

		# While there is a match, continue matching
		while (target[skip + i] == pattern[i]):
			if i == 0:
				return skip
			else:
				pass
			i = i - 1

		# Address skip table since a mismatch is found
		skip = skip + skip_table[target[skip + len(pattern) - 1]]
	
	# Pattern is not found
	return -1



# Test the BMH algorithm
mat = match_search("brefbe", "abadfdfdsdjslbrefbey")
print mat

mat = match_search("safdas","")
print mat