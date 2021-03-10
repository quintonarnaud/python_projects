"""
    File : fake-news-ms.py
    Author : Quinton Arnaud
    Purpose : Iterates through a CSV file and sorts article title data into a list of Word objects based on the word used and the
    number of times the word appears. With a given N, can print out words with a count greater than that at the Nth highest count. 
    Uses merge sort to first sort by count and then sort by alphabetical.
"""
import csv
import string
import sys

sys.setrecursionlimit(2500)

class Word:
	"""Object representing words"""
	def __init__(self, word):
		self._word = word
		self._count = 1

	def word(self):
		return self._word

	def count(self):
		return self._count

	def incr(self):
		self._count += 1

	def __str__(self):
		return self._word

def merge(l1, l2, merged):
	""" Based on in class merge, sorts by count, if count is equal, sort by alpha word
		
		Parameters: two lists and a merging of lists for recursion

		Returns: Either sorted merged list, or recursively called to sort again"""
	if l1 == [] or l2 == []:
		return merged + l1 + l2 #sorted
	else:
		if l1[0]._count > l2[0]._count: #if higher count
			newmerged = merged + [l1[0]]
			newl1 = l1[1:]
			newl2 = l2
		else:
			if l1[0]._count == l2[0]._count and l1[0]._word < l2[0]._word: #if same count treat comparison with alphas
				newmerged = merged + [l1[0]]
				newl1 = l1[1:]
				newl2 = l2
			else:
				newmerged = merged +[l2[0]] #lower count and alpha
				newl1 = l1
				newl2 = l2[1:]
		return merge(newl1, newl2, newmerged) #recursively call to continue sorting

def msort(L):
	""" Taken from class msort
		
		Parameters: unsorted list

		Returns: sorted list"""
	if len(L) <= 1:
		return L #already sorted
	else:
		split = len(L) // 2
		l1 = L[:split]
		l2 = L[split:]
		sortedl1 = msort(l1) #split and merge until sorted
		sortedl2 = msort(l2)
		return merge(sortedl1, sortedl2, []) #merge final two lists to be sorted

def main():

	WordList = []
	filename = input("File: ")

	try: #try to open file
		sfile = open(filename)
	except:
		print("ERROR: Could not open file " + filename)
		raise SystemExit

	csvreader = csv.reader(sfile) #parse as csv file

	for slist in csvreader:

		if slist[0][0] == '#': #ignore comment line
			continue

		title = slist[4] #get title at index 4

		for char in string.punctuation: #replace all punctuation with a space
			title = title.replace(char, " ")

		title = title.lower().split() 

		title = [ word for word in title if len(word) > 2 ] # only keep words that have a lenght greater than 2

		for word in title: # go thru all words
			flag = 0
			if WordList == []:
				WordList.append(Word(word)) #add word if list empty
				continue
			for node in WordList:
				if node._word == word: #if word already in list, increment count
					node.incr()
					flag = 1
					break
			if flag == 0: #if word was not found in list, add to list
				WordList.append(Word(word))

	WordList = msort(WordList) #sort

	n = input("N: ")

	try:
		n = int(n) #make sure n is a readable integer
	except:
		print("ERROR: Could not read N")
		raise SystemExit

	assert n >= 0 # make sure non negative n

	for node in WordList:
		if node._count >= WordList[n]._count: #print up to the count of the node found at index n
			print(node._word +" : "+ str(node._count))
		else:
			break
main()










