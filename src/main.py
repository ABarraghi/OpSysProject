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
parser.add_argument("-F", "--feedback", action="store_true", help="Use the feedback job scheduler")

# parse args
args = parser.parse_args()

#check arguments
if (args.input and (not os.path.exists(args.input)) ): #if input file does not exist
    parser.error("--input file does not exist")
elif (args.input and (not args.input.lower().endswith(".json"))) : #if filename is not json
    parser.error("The program only accepts json file types")
if (args.roundrobin == False) and (args.feedback == False): #if no job scheduler is picked
    parser.error("The program requires a job scheduler to run")
if (args.realtime and ((args.roundrobin == False) and (args.feedback == False))): #if --realtime is used without a job scheduler
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

        temp.setIdentifier(json_data[elem]["identifier"])
        temp.setState(json_data[elem]["state"])
        temp.setPriority(json_data[elem]["priority"])
        temp.setPc(json_data[elem]["pc"])
        temp.setMemoryPointers(json_data[elem]["memory_pointers"])
        temp.setContextData(json_data[elem]["context_data"])
        temp.setIOStatusInfo(json_data[elem]["io_status_info"])
        temp.setGlobalTimer(json_data[elem]["global_timer"])
        temp.setContext(json_data[elem]["context"])

        job_list.append(temp)

    return job_list

#----------------------------------------------------------------------------------------------------------

my_jobs = []
dump_list = []
job_list = LinkedList()

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
if (args.roundrobin or args.feedback):
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
            max = job_list.getMaxPriority() #update priority

            if cur_node.data.getPriority() == max:
                #set to running
                cur_node.data.setState("running")
                if args.feedback:
                    timeslice *= cur_node.data.getFeedbackProgress()
                    cur_node.data.feedbackUpdate()

                copyTimeslice = timeslice
                #if timeslice is greater than time remaining, then add the difference instead of timeslice by temporarily setting timeslice to said difference
                if((cur_node.data.getCpuTimeToComplete() - cur_node.data.getCpuTimeCompleted()) < timeslice):
                    timeslice = cur_node.data.getCpuTimeToComplete() - cur_node.data.getCpuTimeCompleted()

                #simulate realtime console
                if args.realtime:
                    temp_timer = 0 #tracks both definitions of time
                    temp_timer2 = 0 #tracks only TIME_UNIT
                    
                    temp = definitions.CST
                    if (job_list.get_length() == 1):    #if there is only one job in queue, don't add CST
                        temp = 0

                    while(temp_timer <= (timeslice + temp)):

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"""
    GLOBAL TIME: {global_timer + temp_timer}
    JOB NUMBER: {cur_node.data.getIdentifier()}
    TIMER: {cur_node.data.getCpuTimeCompleted() +  temp_timer2} / {cur_node.data.getCpuTimeToComplete()}
    TIME SPENT WAITING: {cur_node.data.getTimeSpentWaiting()}
    """, end='\r')
                        #prepare for next second
                        #time.sleep(1)
                        temp_timer += 1
                        if (temp_timer2 + 1 <= timeslice):
                            temp_timer2 += 1
                    temp_timer = 0
                    temp_timer2 = 0


                    #add CST and TIME_UNIT to global_timer and add TIME_UNIT to job_list.get_node_data_at()
                    if(cur_node.data.getTimeEnteredToQueue() == 0):
                        cur_node.data.setTimeEnteredToQueue(global_timer)
                    if(cur_node.data.getTimeStartedOnCpu() == 0):
                        cur_node.data.setTimeStartedOnCpu(global_timer)

                    #global timer
                    global_timer += timeslice
                    if (job_list.get_length() != 1):    #if there is only one job in queue, don't add CST
                        global_timer += definitions.CST

                    #job timers
                    cur_node.data.addCpuTimeCompleted(timeslice)

                    #add time spent waiting to all jobs except current job (not done yet)
                    temp_node = cur_node
                    while True:
                        if (job_list.get_length() != 1):
                            cur_node.data.addToTimeSpentWaiting(definitions.CST)
                        cur_node.data.addToTimeSpentWaiting(timeslice)
                        cur_node = cur_node.next
                        if temp_node == cur_node:
                            break

                    #reset timeslice
                    timeslice = copyTimeslice

                    #set to not running
                    cur_node.data.setState("not_running")

                    #update global timer in Job object
                    for i in range(job_list.get_length()):
                        cur_node.data.setGlobalTimer(global_timer)
                    
                    #check if job is completed. if true, remove job off the job list (skip it) and declare the global time completed
                    if (cur_node.data.getCpuTimeCompleted() >= cur_node.data.getCpuTimeToComplete() ):
                        cur_node.data.setTimeCompleted(global_timer)

                        dump_list.append(cur_node.data.toDict())
                        delteted = cur_node.data
                        cur_node = cur_node.next
                        job_list.delete(delteted)
                        #print("FLAG1: len after:", job_list.get_length())

            cur_node = cur_node.next
                    

    except KeyboardInterrupt: #if ctrl+c is pressed
        #dump job information to log.json
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
