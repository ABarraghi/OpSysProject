#LinkedList.py
#A singly-linked LinkedList data structure for general objects
#First created Feb 14 2025
#Last modified Feb 14 2025
from include.node import Node

class LinkedList:

    head = None
    length = 0

    #intitalizing by an array of Nodes
    #Assuming a non-zero LL size
    def __init__(self,nodeList):

        self.head = Node(nodeList[0])
        cur = self.head

        self.length = 1

        for i in range(1,len(nodeList)):
            cur.next = Node(nodeList[i])
            cur = cur.next
            self.length += 1

    
    #Go through the LL, starting from the head
    def to_string(self):
        print(f"LinkedList of size : {self.length}")
        cur = self.head

        counter = 1

        while cur is not None:
            print(f"Node #{counter} : ",cur)
            cur = cur.next
            counter = counter + 1



    




