#LinkedList.py
#A singly-linked LinkedList data structure for general objects
#First created Feb 14 2025
#Last modified Feb 15 2025
from include.node import Node

class LinkedList:

    #Intitalizing by an array of Nodes
    def __init__(self,nodeList):

        self.head = None
        self.tail = None
        self.length = len(nodeList)

        if(self.length > 0):

            self.head = Node(nodeList[0])
            cur = self.head

            for i in range(1,len(nodeList)):

                cur.next = Node(nodeList[i])
                cur = cur.next
            
            self.tail = cur
            
    
    #Go through the LL, starting from the head
    def to_string(self):

        print(f"LinkedList of size : {self.length}")
        cur = self.head

        counter = 1

        while cur is not None:

            print(f"Node #{counter} : ",cur)
            cur = cur.next
            counter = counter + 1

    #Add Node at the end of the LinkedList
    def append(self,node):

        self.tail.next = node
        self.tail = node
        self.length += 1

    #Remove Node at the end of the LinkedList
    def remove_last(self):

        counter = 0
        cur = self.head
        
        if(self.length == 0):
            raise IndexError("attempted removal on empty linked list")

        while(counter < (self.length-2)):

            cur = cur.next
            counter += 1

        cur.next = None
        self.tail = cur
        self.length -= 1
    
    #Add Node at a specified index
    def insert_at(self,index,node):

        if((index > self.length) or (index < 0)):
            raise IndexError("chosen index is out of bounds")

        counter = 0
        target_node = self.head

        #stop at the node right before specified index
        while(counter < (index-1)):

            target_node = target_node.next
            counter += 1
        
        #target_node is the node prior to the one inserted
        #after_node is the node after the one inserted
        after_node = target_node.next
        target_node.next = node
        node.next = after_node

        self.length += 1

        #update head and tail as needed
        if(index == 0):
            self.head = node

        if(index == (self.length-1)):
            self.tail = node

        

    #All of the following functions are zero-indexed

    def get_node_at(self,index):

        if((index > self.length) or (index < 0)):
            raise IndexError("chosen index is out of bounds")

        counter = 0
        target_node = self.head

        while(counter < index):

            target_node = target_node.next
            counter += 1
        
        return target_node

    def set_node_at(self,index,node):

        if((index > self.length) or (index < 0)):
            raise IndexError("chosen index is out of bounds")

        counter = 0
        target_node = self.head

        #stop at the node right before specified index
        while(counter < (index-1)):

            target_node = target_node.next
            counter += 1
        
        #target_node is the node prior to the one inserted
        #replaced_node is the node that will be overriden by this method
        replaced_node = target_node.next
        node.next = replaced_node.next
        target_node.next = node

    def get_node_data_at(self,index):

        return self.get_node_at(index).data

    def set_node_data_at(self,index,data):

        if((index > self.length) or (index < 0)):
            raise IndexError("chosen index is out of bounds")

        counter = 0
        target_node = self.head

        #stop at the node right before specified index
        while(counter < (index-1)):

            target_node = target_node.next
            counter += 1
        
        target_node.next.data = data
        


