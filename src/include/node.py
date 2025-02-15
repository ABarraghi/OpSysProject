#Node.py
#Defining a Node object for use in the LinkedList
#First created Feb 14 2025
#Last modified Feb 14 2025
class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"This Node's Data: {self.data}."