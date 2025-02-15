#LinkedList.py
#A singly-linked LinkedList data structure for general objects
#First created Feb 14 2025
#Last modified Feb 14 2025
from include.node import Node

class linkedlist:

    head = None

    #intitalizing by an array of Nodes
    #Assuming a non-zero size of LL
    def __init__(self,nodeList):

        self.head = Node(nodeList[0])
        cur = self.head
        counter = 0

        for element in range(len(nodeList)):
            cur.next = Node(element)
            cur = cur.next
    
    #Go through the LL, starting from the head
    def to_string(self):
        cur = self.head

        counter = 1

        while cur is not None:
            print(f"Node #{counter} : ",cur)
            cur = cur.next
            counter = counter + 1



    




