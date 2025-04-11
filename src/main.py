import time
import os
import sys

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
parser.add_argument("--realtime", action="store_true", help="Run the program in real time")
parser.add_argument("-T", "--test", action="store_true", help="Run the test code in the program")
parser.add_argument("-S", "--timeslice", type=int, help="Change the timeslice, type int, default: 10")

# parse args
args = parser.parse_args()

#check arguments
if (args.input and (not os.path.exists(args.input)) ): #if input file does not exist
    parser.error("--input file does not exist")
elif (args.input and (not args.input.lower().endswith(".json"))) : #if filename is not json
    parser.error("The program only accepts json file types")
if args.roundrobin == False: #if no job scheduler is picked
    parser.error("The program requires a job scheduler to run")
if (args.realtime and (args.roundrobin == False)): #if --realtime is used without a job scheduler
    parser.error("The --realtime argument requires a job scheduler")

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
        temp.setGlobalTimer(json_data[elem-1]["global_timer"])
        temp.setContext(json_data[elem-1]["context"])

        job_list.append(temp)

    return job_list

#----------------------------------------------------------------------------------------------------------

my_jobs = []
dump_list = []
job_list = LinkedList()

my_iter = 0
skip_bool = False

temp = None

#----------------------------------------------------------------------------------------------------------
# Define file input
if args.input:
    file_input = args.input
else:
    file_input = definitions.INPUT_FILE


# Define timeslice
if args.timeslice:
    timeslice = args.timeslice
else:
    timeslice = definitions.TIME_UNIT
#----------------------------------------------------------------------------------------------------------

# round robin scheduler code
if args.roundrobin:
    #declare the job list
    my_jobs = defineJobs(file_input)

    #start the LinkedList
    for i in range(len(my_jobs)):
        job_list.insert_at_beginning(my_jobs[i])

    cur_node = job_list.head

    #define global timer
    global_timer = cur_node.data.getGlobalTimer()

    try:
        #while loop that completes each job one by one
        while (job_list.get_length() > 0):
            max = job_list.getMaxPriority()
            for i in reversed(range(1, max+1)):
                max = job_list.getMaxPriority()
                if cur_node.data.getPriority() == i:
                    #never gets here
                    pass

    except KeyboardInterrupt: #if ctrl+c is pressed
        #dump job information to log.json
        dump_list = []
        #set global_timer
        for i in range(job_list.get_length()):
            cur_node.data.setGlobalTimer(global_timer) 
            cur_node = cur_node.next

        #turn job_list job objects into dicts and send that to dump_list, 
        for i in range(job_list.get_length()):
            dump_list.append(cur_node.data.toDict())
            cur_node = cur_node.next

        with open("log.json", "w") as log:
            json.dump(dump_list, log, indent=4)
        print("SIMULATION INTERRUPTED, CURRENT DATA WRITTEN TO LOG.JSON. EXITING PROGRAM...")
        sys.exit()


    #dump job information to log.json if program completes
    for i in range(len(dump_list)):
        dump_list[i]["global_timer"] = global_timer
    temp = json.dumps(dump_list, indent=4)
    with open("log.json", "w") as log:
        json.dump(dump_list, log, indent=4)
    print("SIMULATION COMPLETED, CURRENT DATA WRITTEN TO LOG.JSON. EXITING PROGRAM...")
    sys.exit()
        
#----------------------------------------------------------------------------------------------------------
