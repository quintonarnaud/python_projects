"""
    File : rhymes-oo.py
    Author : Quinton Arnaud
    Purpose : An input file of a Pronunciation Dictionary is read in and a user inputed word is read in. All words in the dictionary that form
    a perfect rhyme with the inputed word will be printed out. The program is written in an OO manner.
"""
class Word:
	""" Word objext storing the string of the word and the list/list of lists of its' pronunciations """
	def __init__(self, word, pron):
		self._word = word
		self._pronunciations = pron

	def addPron(self, pron):
		""" Turns self._pronunciations into a lists of lists and appends new pronunciation list
  
    		Parameters: self, new pronunciation
  
    		Returns: void """
		self._pronunciations = [self._pronunciations]
		self._pronunciations.append(pron)

	def getPron(self):
		return self._pronunciations

	def getName(self):
		return self._word

	def __eq__(self, wordObj): #determine if rhyme
		""" Turns equality operator between two word objects into a boolean value based on whether or not they are perfect rhymes
  
    		Parameters: self, word object
  
    		Returns: True if perfect Rhymes, False if not """
		index2 = 0
		index1 = 0
		if isinstance(self._pronunciations[0], list): #if multiple pronunciations in self
			for prons1 in self._pronunciations: #go through each pronunciation in self
				index1 = 0
				for pron1 in prons1:
					if "1" in pron1: #find index of primary stress phoneme
						break
					index1 += 1

				if isinstance(wordObj.getPron()[0], list): # if multiple pronunciations
					for prons2 in wordObj.getPron(): #compare each pronunciation in self with each pron in wordObj
						for pron2 in prons2:
							if "1" in pron2: #finding primary stress

								if prons1[index1:] == prons2[index2:]: #equal stress phonemes and equal subsequent sounds
									if ((index1 == 0 and index2 != 0) or (index1 != 0 and index2 == 0) or #different phonemes preceeding stress phoneme
										(index1 != 0 and index2 != 0 and prons1[index1-1] != prons2[index2-1])):
										return True # words rhyme
								index2 = 0
								break
							index2 += 1
				else: #one pronunciation in wordObj
					for pron2 in wordObj.getPron():
							if "1" in pron2: #finding primary stress

								if prons1[index1:] == wordObj.getPron()[index2:]: #equal stress phonemes and equal subsequent sounds
									if ((index1 == 0 and index2 != 0) or (index1 != 0 and index2 == 0) or #different phonemes preceeding stress phoneme
										(index1 != 0 and index2 != 0 and prons1[index1-1] != wordObj.getPron()[index2-1])):
										return True # words rhyme
							index2 += 1
		else: #one pronunciation in self
			for pron1 in self._pronunciations:
				if "1" not in pron1: #find index of primary stress phoneme
					index1 += 1
					continue # continues for loop until primary stress is found

				if isinstance(wordObj.getPron()[0], list): # if multiple pronunciations
					for prons2 in wordObj.getPron(): #compare each pronunciation in self with each pron in wordObj
						for pron2 in prons2:
							if "1" in pron2: #finding primary stress
								if self._pronunciations[index1:] == prons2[index2:]: #equal stress phonemes and equal subsequent sounds
									if ((index1 == 0 and index2 != 0) or (index1 != 0 and index2 == 0) or #different phonemes preceeding stress phoneme
										(index1 != 0 and index2 != 0 and self._pronunciations[index1-1] != prons2[index2-1])):
										return True # words rhyme
								index2 = 0
								break
							index2 += 1
				else: #one pronunciation in wordObj
					for pron2 in wordObj.getPron():
							if "1" in pron2: #finding primary stress

								if self._pronunciations[index1:] == wordObj.getPron()[index2:]: #equal stress phonemes and equal subsequent sounds

									if ((index1 == 0 and index2 != 0) or (index1 != 0 and index2 == 0) or #different phonemes preceeding stress phoneme
										(index1 != 0 and index2 != 0 and self._pronunciations[index1-1] != wordObj.getPron()[index2-1])):
										return True # words rhyme
							index2 += 1
				break
		return False # words dont rhyme

	def __str__(self):
		return self._word

class WordMap:
	def __init__(self):
		self._wordMap = {}

	def initWordMap(self):
		""" Initializes word map with inputed pronunciation dictionary
  
    		Parameters: self
  
    		Returns: Void """
		fname = input()
		try: # try to open file
			sfile = open(fname)

		except: # report error and exit program if file couldn't be opened
			print("ERROR: Could not open file " + fname)
			raise SystemExit

		prevWord = ""

		for i in sfile:
			line = i.lower().rstrip().split()

			if line[0] == prevWord: # if word already present in dictionary (multiple pronunciations)
				self._wordMap[line[0]].addPron(line[1:])

			else:	# creating new word obj
				self._wordMap[line[0]] = Word(line[0], line[1:])
				prevWord = line[0] # for testing whether or not theres multiple pronunciations

	def getRhymes(self):
		""" Goes through the word map and prints all words that rhyme with user input word
  
    		Parameters: self
  
    		Returns: Void, but prints rhymes """
		word = input()
		try: # test if word is in the wordmap
			self._wordMap[word]
		except: # report error and exit if not
			print("ERROR: the word input by the user is not in the pronunciation dictionary " + word)
			raise SystemExit

		for words in self._wordMap:
			if self._wordMap[word] == self._wordMap[words]: # using equality operator defined in Word class
				print(words.lower())

	def __str__(self):
		return self._wordMap

def main():
	wordmap = WordMap()
	wordmap.initWordMap()
	wordmap.getRhymes()

main()
