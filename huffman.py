"""
    File : huffman.py
    Author : Quinton Arnaud
    Purpose : Given the preorder and inorder of a tree, recursively create the tree, recursively print
    the postorder of the tree, decode a binary encoding of the tree and print
"""
class BinarySearchTree:
	def __init__(self, head):
		self._value = None
		self._left = None
		self._right = None
		self._ishead = head # boolean to tell if at head of node

	def construct(self, preorder, inorder):
		""" Recursively constructs a tree given the pre- an in- order
	  
		Parameters: self, 2 list of integers of the pre- and in- order

		Returns: recursively returns to create tree """

		if len(preorder) == 0 or len(inorder) == 0: #base case/finished recursive
			return

		self._value = preorder[0]

		lefttree = inorder[:inorder.index(preorder[0])] #left side of tree
		righttree = inorder[inorder.index(preorder[0]):] #right side of tree
		if righttree != []:
			righttree.remove(preorder[0]) #remove parent node from righttree

		if len(lefttree) != 0: #if more values on left side
			self._left = BinarySearchTree(False) #create node, false since not head node
			self._left.construct(preorder[1:], lefttree) #preorder moves on, inorder gets left side of tree
		
		if len(righttree) != 0: #if no more values on left side for given node
			self._right = BinarySearchTree(False)

			while preorder[0] not in righttree: #move the preorder up intil it is in the right place relative to the 
				preorder = preorder[1:]			#current right side of tree

			self._right.construct(preorder, righttree) #inorder is now right side of tree

		return # returns when at a leaf node

	def decode(self, encoder):
		""" Decode a tree given an encoder and print leaf node values from encoder
	  
	    Parameters: self, string of binary number of length n
	  
	    Returns: None, prints decoded number """

		head = self # set head
		for bit in encoder: # go thru string
			if bit == "0":
				if self._left == None: #if invalid move restart at head
					self = head
				else:
					self = self._left #move left
					if self._left == None and self._right == None: #if at leaf node
						print(self._value, end="") #print and restart at head
						self = head

			elif bit == "1":
				if self._right == None: #if invalid move restart at head
					self = head
				else:
					self = self._right
					if self._left == None and self._right == None:
						print(self._value, end="")
						self = head

	def printpostorder(self):
		""" Prints post order of a tree
	  
	    Parameters: self
	  
	    Returns: None, prints decoded number """
		if self._value == None: #base case/end of current recursion
			return
		if self._left != None:
			self._left.printpostorder() # LEFT nodes first
		if self._right != None:
			self._right.printpostorder() # RIGHT nodes second
		if self._ishead == False:
			print(self._value, end =" ") # NODEs last
		else:
			print(self._value)

	def __str__(self): #str special function to help with debugging (from short prob)
		if self._value == None:
			return "None"
		else:
			return "(" + str(self._value) +" "+ str(self._left) +" "+ str(self._right) + ")"

def init():
	""" Processes file and calls functions on tree
  
    Parameters: None
  
    Returns: None """
	fname = input("Input file: ")

	try: #try to open
		sfile = open(fname)
	except:
		print("ERROR: Could not open file " + fname)
		raise SystemExit

	i = 0 
	for line in sfile: #assign each line to their respective data
		if i == 0:
			preorder = line.strip().split()
			i+=1
		elif i == 1:
			inorder = line.strip().split()
			i+=1
		elif i == 2:
			encoded = line.strip()

	tree = BinarySearchTree(True) #create tree, True since head of tree

	tree.construct(preorder, inorder) #construct the tree

	tree.printpostorder() #print the postorder of tree
	tree.decode(str(encoded)) #decode the tree and print decoded value
	print() #print newline

init()