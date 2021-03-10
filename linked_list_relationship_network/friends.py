"""
    File : friends.py
    Author : Quinton Arnaud
    Purpose : Using linked list implementation in LinkedList.py, create friend relationship network and print mutual
    friends given the name of two users.
"""
from linked_list import *

def init():
	""" Initialize file of names into relationship linked list
  
    Parameters: none
  
    Returns: relations, linked list of users and their friends """
	filename = input("Input file: ")

	try:
		sfile = open(filename) # try to open file
	except:
		print("ERROR: Could not open file " + filename) # report and quit if cant open
		raise SystemExit

	relations = LinkedList()
	for line in sfile:
		names = line.strip().split()
		relations.addRelation(names[0], names[1]) # adds relation of first person as user and second as friend
		relations.addRelation(names[1], names[0]) # now second person is user and first person is friend

	return relations # return linked list

def mutual_friends(relations):
	""" Iterate through relations linked list and their friends linked list to find mutual friends given two users
  
    Parameters: relations, linked list
  
    Returns: void, but prints mutual friends if found """
	try:
		name1 = input('Name 1: ').strip() # try to read in names
		name2 = input('Name 2: ').strip()
	except:
		return

	if name1 not in relations: # if either name is not a user in relations
		print( "ERROR: Unknown person " + name1)
		return
	if name2 not in relations:
		print( "ERROR: Unknown person " + name2)
		return

	curnode = relations._head # find nodes of users name1 and name2
	while curnode != None:
		if curnode._name == name1:
			name1Node = curnode
		if curnode._name == name2:
			name2Node = curnode

		curnode = curnode._next

	nameFound = False # name has not been found yet
	curnode = name1Node._friends._head
	while curnode != None: # go thru name1's friends

		if curnode._name in name2Node._friends: # if name1 friend is in friend list of name 2

			if nameFound == False: # print friends in common once if a friend is found
				print("Friends in common:")
				nameFound = True

			print(curnode._name) # print mutual friend 

		curnode = curnode._next

def main():

	mutual_friends(init())

main()