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
        temp.setGlobalTimer(json_data[elem-1]["global_timer"])
        temp.setContext(json_data[elem-1]["context"])

        job_list.append(temp)

    return job_list

#----------------------------------------------------------------------------------------------------------

my_jobs = []
dump_list = []
job_list = None

my_iter = 0
skip_bool = False

temp = None

#----------------------------------------------------------------------------------------------------------
# Define file input
if args.input:
    file_input = args.input
else:
    file_input = definitions.INPUT_FILE
#----------------------------------------------------------------------------------------------------------

# round robin scheduler code
if args.roundrobin:
    #declare the job list
    my_jobs = defineJobs(file_input)

    #start the LinkedList
    job_list = LinkedList(my_jobs)
    my_jobs = []

    #define global timer
    global_timer = job_list.get_node_data_at(0).getGlobalTimer()

    try:
        #while loop that completes each job one by one
        while (job_list.get_length() > 0):
            #debugging
            #print(job_list.get_length())

            #check if job is completed. if true, remove job off the job list (skip it) and declare the global time completed
            if (job_list.get_node_data_at(my_iter).getCpuTimeCompleted() >= job_list.get_node_data_at(my_iter).getCpuTimeToComplete() ):
                job_list.get_node_data_at(my_iter).setTimeCompleted(global_timer)

                #add my_iter to completed jobs
                dump_list.append(job_list.get_node_data_at(my_iter).toDict())
                job_list.remove_at(my_iter)

                skip_bool = True

            if (skip_bool == False):
                #set to running
                job_list.get_node_data_at(my_iter).setState("running")

                #simulate realtime console
                if args.realtime:
                    temp_timer = 0 #tracks both definitions of time
                    temp_timer2 = 0 #tracks only TIME_UNIT
                    
                    temp = definitions.CST
                    if (job_list.get_length() == 1):    #if there is only one job in queue, don't add CST
                        temp = 0

                    while(temp_timer <= (definitions.TIME_UNIT + temp)):

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"""
GLOBAL TIME: {global_timer + temp_timer}
JOB NUMBER: {job_list.get_node_data_at(my_iter).getIdentifier()}
TIMER: {job_list.get_node_data_at(my_iter).getCpuTimeCompleted() +  temp_timer2} / {job_list.get_node_data_at(my_iter).getCpuTimeToComplete()}
TIME SPENT WAITING: {job_list.get_node_data_at(my_iter).getTimeSpentWaiting()}
""", end='\r')
                        #prepare for next second
                        time.sleep(1)
                        temp_timer += 1
                        if (temp_timer2 + 1 <= definitions.TIME_UNIT):
                            temp_timer2 += 1
                temp_timer = 0
                temp_timer2 = 0

                #add CST and TIME_UNIT to global_timer and add TIME_UNIT to job_list.get_node_data_at()
                if(job_list.get_node_data_at(my_iter).getTimeEnteredToQueue() == 0):
                    job_list.get_node_data_at(my_iter).setTimeEnteredToQueue(global_timer)
                if(job_list.get_node_data_at(my_iter).getTimeStartedOnCpu() == 0):
                    job_list.get_node_data_at(my_iter).setTimeStartedOnCpu(global_timer)

                #global timer
                global_timer += definitions.TIME_UNIT
                if (job_list.get_length() != 1):    #if there is only one job in queue, don't add CST
                    global_timer += definitions.CST

                #job timers
                job_list.get_node_data_at(my_iter).addCpuTimeCompleted(definitions.TIME_UNIT)
                if (job_list.get_length() != 1):    #if there is only one job in queue, don't add CST
                    job_list.get_node_data_at(my_iter).addToTimeSpentWaiting(definitions.CST)

                #set to not running
                job_list.get_node_data_at(my_iter).setState("not_running")

                #update global timer in Job object
                for i in range(job_list.get_length()):
                    job_list.get_node_data_at(i).setGlobalTimer(global_timer)
            skip_bool = False

            #go on to the next job
            my_iter += 1
            if (my_iter > (job_list.get_length() - 1)):
                my_iter = 0
            if (job_list.get_length() == 1):
                my_iter = 0 
            #print("Updated my_iter: " + str(my_iter))
    except KeyboardInterrupt: #if ctrl+c is pressed
        #dump job information to log.json
        dump_list = []
        #turn job_list job objects into dicts and send that to dump_list, 
        for i in range(job_list.get_length()):
            dump_list.append(job_list.get_node_data_at(i).toDict())

        with open("log.json", "w") as log:
            json.dump(dump_list, log, indent=4)
        print("SIMULATION INTERRUPTED, CURRENT DATA WRITTEN TO LOG.JSON. EXITING PROGRAM...")
        sys.exit()


    #dump job information to log.json if program completes
    for job in my_jobs:
        dump_list.append(job.toDict())

    temp = json.dumps(dump_list, indent=4)
    with open("log.json", "w") as log:
        json.dump(dump_list, log, indent=4)
    print("SIMULATION COMPLETED, CURRENT DATA WRITTEN TO LOG.JSON. EXITING PROGRAM...")
    sys.exit()
        
#----------------------------------------------------------------------------------------------------------
if args.test:
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

    tester.remove_at(4)
    tester.to_string()
    #print(tester.head)

    #secondtest = tester.head.next
    #print(secondtest)


    #testnode = Node(5)
    #print(testnode)