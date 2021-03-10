"""
	File : writer-bot-ht.py
	Author : Quinton Arnaud
	Purpose : Generate text based off of a given text, size of hash table, number of prefixes, and length of text using hash ADT. 
"""
import random

# constants
NONWORD = "@"
SEED = 8

class Hashtable:
	def __init__(self, size):
		"""Initialize hash table with None elements
  
    	Parameters: size of table
  
		Returns: None"""
		self._pairs = [None]*size
		self._size = size

	def put(self, key, value):
		"""Places key value pair into hash table or appends value to existing key
  
    	Parameters: key, value
  
   		Returns: None"""
		index = self._hash(key) #get index

		while self._pairs[index] != None: # while linear probing is possible placement
			if self._pairs[index][0] == key: # if found key, found index
				break
			if index == 0: # allows to loop around table
				index == self._size - 1
			else:
				index -= 1 #linear probe

		if self._pairs[index] == None: # if key not found
			self._pairs[index] = [None]*2 #create key value placement
			self._pairs[index][0] = key
			self._pairs[index][1] = [value]

		elif self._pairs[index][0] == key: # if key found append
			self._pairs[index][1].append(value)

	def get(self, key):
		""" Gets values of key or returns non if not found
  
    	Parameters: key to find
  
    	Returns: None or values"""
		index = self._hash(key)
		delta = 0
		while self._pairs[index] != None: #while linear probing is possible
			if self._pairs[index][0] == key: 
				return self._pairs[index][1] # found key
			index -= 1
			delta += 1
			if delta > self._size: # index decrement check for infinite looping
				return None
		return None

	def __contains__(self, key):
		""" Tells if contains, essentially same as get() w/ different returns
  
    	Parameters: key to find
  
    	Returns: Boolean"""
		index = self._hash(key)
		delta = 0
		while self._pairs[index] != None:
			if self._pairs[index][0] == key:
				return True
			index -= 1
			delta += 1
			if delta > self._size:
				return False
		return False

	def __str__(self):
		return str(self._pairs)

	def _hash(self, key):
		""" Calcualtes hash keys
  
    	Parameters: key string
  
    	Returns: hash code"""
		p = 0
		for c in key:
			p = 31*p + ord(c)
		return p % self._size

def init():
	"""Initialize file into data elements
  
    Parameters: None
  
    Returns: list of all words in given file
  
    Pre-condition: Valid filename and file given
  
    Post-condition: list of strings in order of given text"""

	filename = input()
	try:
		sfile = open(filename)
	except:
		print("ERROR: Could not open file " + filename) # report and quit if cant open
		raise SystemExit

	reference = []

	for line in sfile:
		line = line.rstrip().split() # create list of all strings in text

		reference += line

	return reference 

def CreateTable(reference):
	"""Uses a list of strings and an inputed number of prefixes to create a dictionary of tuple prefix keys and list of suffix items
  
    Parameters: List of strings
  
    Returns: Dictionary with tuple keys and list items
  
    Pre-condition: Valid reference list and a prefix size > 0
  
    Post-condition: Dictionary has been created"""

	M = int(input())
	htable = Hashtable(M)

	global prefixSize
	prefixSize = int(input())
	prefix = []

	if prefixSize <= 0:
		print("ERROR: specified prefix size is less than one")
		raise SystemExit

	for j in range(prefixSize): # initialize number of prefixes and suffix to NONWORD
		prefix.append(NONWORD)
	suffix = NONWORD

	for i in reference: # for the entire list

		prefix.append(suffix) # iterate the prefix list forward
		prefix.pop(0)
		suffix = i # set the suffix as the current string

		key = " ".join(prefix)
		htable.put(key, suffix)

	return htable

def generate(htable):
	"""Generates and prints, 10 words per line, text based off given table dictionary
  
    Parameters: Dictionary with tuple keys and list items
  
    Returns: Void
  
    Pre-condition: Valid dictionary and a text size > 0
  
    Post-condition: Text has been printed"""

	textSize = int(input())
	if textSize <= 0:
		print("ERROR: specified size of the generated text is less than one")
		raise SystemExit

	random.seed(SEED)

	# find number of prefixes
	key = []
	for i in range(prefixSize):
		key.append(NONWORD)
	keyStr = " ".join(key)

	text = []
	for i in range(textSize): # go until text size is reached or until last suffix found
		if keyStr in htable:
			value = htable.get(keyStr)
			if len(value) != 1:
				index = random.randint(0, len(value)-1) # finding random index for suffix list of given prefix keys
			else:
				index = 0
			text.append(value[index]) # append word to text list

			key.append(value[index]) # get new keys
			key.pop(0)
			keyStr = " ".join(key)

		else:
			break

	count = 1 # printing in correct fashion, 10 words per line, last word has newline regardless
	for i in range(len(text)):
		if i == len(text) - 1:
			print(text[i])
		elif count == 1:
			print(text[i], end = " ")
		elif count % 10 != 0:
			print(text[i], end = " ")
		else:
			print(text[i], end = "\n")
		count += 1

def main():
	generate(CreateTable(init()))

main()