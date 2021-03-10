"""
    File : linked_list.py
    Author : Quinton Arnaud
    Purpose : Holds classes to create linked list and node objects in friends.py
"""
class Node:
	def __init__(self, name):
		""" Initialize user node
  
    	Parameters: self, name of user
  
    	Returns: void """
		self._name = name
		self._next = None
		self._friends = None

	def name(self):
		return self._name

	def __str__(self):
		return self._name

class LinkedList:
	def __init__(self):
		self._head = None 

	def addRelation(self, name, friend):
		""" Adds relation in linked list, if user is in list, add friend if not already have that friend, else add user and friend
  
    	Parameters: self, name of user and friend
  
    	Returns: void """

		curnode = self._head
		if curnode == None: # if empty linked list
			self._head = Node(name) # create new user
			self._head._friends = LinkedList() # create linked list of friends
			self._head._friends._head = Node(friend) # add friend node to list of friends
		else:
			while curnode != None:

				if curnode._name == name: # if user is already in list
					if friend not in curnode._friends: # if user does not already have that friend
						curnode._friends.add(Node(friend)) # add friend to users friendlist
					return
				curnode = curnode._next

			self.add(Node(name)) # else if user is not already in list, add to list
			self._head._friends = LinkedList() # create linked list of friends for user
			self._head._friends._head = Node(friend)

	# taken from ll_sort short prolem
	def add(self, node): # adds node to head of list
		node._next = self._head
		self._head = node

	def __contains__(self, param):
		""" Special function contains to test whether or not a name is in a linked list
  
    	Parameters: self, name of user
  
    	Returns: Boolean if name is in linked list """
		curnode = self._head
		while curnode != None:
			if curnode._name == param: # return true if name is found
				return True
			curnode = curnode._next
		return False