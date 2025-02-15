#LinkedList.py
#A singly-linked LinkedList data structure for general objects
#First created Feb 14 2025
#Last modified Feb 15 2025
from include.node import Node

class LinkedList:

    #Intitalizing by an array of Nodes
    def __init__(self,nodeList):

        self.head = None
        self.length = len(nodeList)

        if(self.length > 0):
            self.head = Node(nodeList[0])
            cur = self.head

            for i in range(1,len(nodeList)):
                cur.next = Node(nodeList[i])
                cur = cur.next

    
    #Go through the LL, starting from the head
    def to_string(self):
        print(f"LinkedList of size : {self.length}")
        cur = self.head

        counter = 1

        while cur is not None:
            print(f"Node #{counter} : ",cur)
            cur = cur.next
            counter = counter + 1

    #Zero-indexed
    def get_node_at(self,index):

        if((index > self.length) or (index < 0)):
            raise IndexError("chosen index is out of bounds")

        counter = 0
        target_node = self.head

        while(counter < index):
            target_node = target_node.next
            counter += 1
        
        return target_node