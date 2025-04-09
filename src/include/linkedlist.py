#LinkedList.py
#A singly-linked LinkedList data structure for general objects
#First created Feb 14 2025
#Last modified Feb 15 2025
from include.node import Node

class LinkedList:

    #Intitalizing by an array of Nodes
    def __init__(self):

        self.head = None
    
    #Insert data with no additional input    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
            self.head = new_node

    #delete where node data = input data
    def delete(self, data):
        if self.head is None:
            print("List is empty!")
            return
        if self.head.data == data:
            if self.head.next == self.head:
                self.head = None
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
            return
        curr = self.head
        prev = None
        while curr.next != self.head:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
        if curr.data == data:
            prev.next = curr.next
        else:
            print("Element not found!")


    #Go through the LL, starting from the head
    def to_string(self):

        print(f"LinkedList of size : {self.length}")
        cur = self.head

        counter = 1

        while cur is not None:

            print(f"Node #{counter} : ",cur)
            cur = cur.next
            counter = counter + 1
    
    #get length of linked list
    def get_length(self):
        if self.head is None:
            return 0
        tempnode = self.head
        length = 0
        while True:
            tempnode = tempnode.next
            length += 1
            if(tempnode == self.head):
                break
        return length
    
    #get highest priority
    def getMaxPriority(self):
        max = 0
        node = self.head
        for i in range(self.get_length()):
            if node.data.getPriority() > max:
                max = node.data.getPriority()
            node = node.next
        return max
