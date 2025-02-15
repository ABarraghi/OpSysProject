import argparse
import json

#include necessary header files
from include import definitions
from include import jobs
from include.linkedlist import LinkedList
from include.node import Node

#----------------------------------------------------------------------------------------------------------

# Create an argparse object
parser = argparse.ArgumentParser(description="Job scheduler simulator")
parser.add_argument("-I", "--input", type=str, help="Use a specific json job file, default is jobs.json")
parser.add_argument("-R", "--roundrobin", action="store_true", help="Use the round robin job scheduler")
# parse args
args = parser.parse_args()

#----------------------------------------------------------------------------------------------------------

#function that automatically takes in the elements in the in put file and converts them into a list of objects
def defineJobs(file_input):
    #load json
    with open(file_input) as json_file:
        json_data = json.load(json_file)

    job_list = []

    #create a Job object for each element in json_data
    for elem in range(len(json_data)):
        temp = jobs.Job()
        #use setters
        temp.setIdentifier(json_data[elem-1]["identifier"])
        temp.setState(json_data[elem-1]["state"])
        temp.setPriority(json_data[elem-1]["priority"])
        temp.setPc(json_data[elem-1]["pc"])
        temp.setMemoryPointers(json_data[elem-1]["memory_pointers"])
        temp.setContextData(json_data[elem-1]["context_data"])
        temp.setIOStatusInfo(json_data[elem-1]["io_status_info"])
        temp.setContext(json_data[elem-1]["context"])

        job_list.append(temp)

    return job_list

#----------------------------------------------------------------------------------------------------------

#set up variables
my_jobs = []

#----------------------------------------------------------------------------------------------------------
# Define file input
if args.input:
    file_input = args.input
else:
    file_input = definitions.INPUT_FILE
# round robin scheduler code
if args.roundrobin:
    from include import roundrobin
    my_jobs = defineJobs(file_input)

#----------------------------------------------------------------------------------------------------------
#Testing LinkedList
tester = LinkedList([1,2,3,4,5])
tester.to_string()

tester_two = LinkedList([1])
tester_two.to_string()

tester_three = LinkedList([])
tester_three.to_string()

tester_four = LinkedList([
        {
            "identifier": 1,
            "state": "not_running",
            "priority": 0,
            "pc": 0,
            "memory_pointers": 0,
            "context_data": 0,
            "io_status_info": 0,
            "context": {
                "cpu_time_to_complete": 100,
                "cpu_time_completed": 0,
                "time_entered_to_queue": 0,
                "time_started_on_cpu": 0,
                "time_spent_waiting": 0,
                "time_completed": 0
            }
        },
        {
            "identifier": 2,
            "state": "not_running",
            "priority": 0,
            "pc": 0,
            "memory_pointers": 0,
            "context_data": 0,
            "io_status_info": 0,
            "context": {
                "cpu_time_to_complete": 300,
                "cpu_time_completed": 0,
                "time_entered_to_queue": 0,
                "time_started_on_cpu": 0,
                "time_spent_waiting": 0,
                "time_completed": 0
            }
        }
])
tester_four.to_string()

tester.set_node_at(2,Node(100))

tester.to_string()
print(tester.get_node_at(2))

tester.set_node_data_at(2,2)
print(tester.get_node_data_at(2))
print(tester.get_node_at(2))

tester.append(Node(6))
tester.to_string()

print(tester.length)

tester.remove_last()
tester.to_string()

tester.remove_last()
tester.to_string()

tester.insert_at(4,Node(5))
tester.to_string()

print(tester.tail)
#print(tester.head)

#secondtest = tester.head.next
#print(secondtest)


#testnode = Node(5)
#print(testnode)