# create a common class object for jobs

class Job:
    def __init__(self):
        self.__identifier = None
        self.__state = None
        self.__priority = None
        self.__pc = None
        self.__memory_pointers = None
        self.__context_data = None
        self.__io_status_info = None
        self.__context = {}

    #setters

    def setIdentifier(self, identifier):
        self.__identifier = identifier

    def setState(self, state):
        self.__state = state
    
    def setPriority(self, priority):
        self.__priority = priority
    
    def setPc(self, pc):
        self.__pc = pc

    def setMemoryPointers(self, memory_pointers):
        self.__memory_pointers = memory_pointers

    def setContextData(self, context_data):
        self.__context_data = context_data

    def setIOStatusInfo(self, io_status_info):
        self.__io_status_info = io_status_info

    def setContext(self, context):
        self.__context = context

        self.__context["cpu_time_to_complete"] = int(self.__context["cpu_time_to_complete"])
        self.__context["cpu_time_completed"] = int(self.__context["cpu_time_completed"])
        self.__context["time_entered_to_queue"] = int(self.__context["time_entered_to_queue"])
        self.__context["time_started_on_cpu"] = int(self.__context["time_started_on_cpu"])
        self.__context["time_spent_waiting"] = int(self.__context["time_spent_waiting"])
        self.__context["time_completed"] = int(self.__context["time_completed"])

    #setters for the context dictionary
    def addCpuTimeCompleted(self, amount):
        self.__context["cpu_time_completed"] += amount

    def setTimeEnteredToQueue(self, time_entered_to_queue):
        self.__context["time_entered_to_queue"] = time_entered_to_queue

    def setTimeStartedOnCpu(self, time_started_on_cpu):
        self.__context["time_started_on_cpu"] = time_started_on_cpu

    def addToTimeSpentWaiting(self, time_spent_waiting):
        self.__context["time_spent_waiting"] += time_spent_waiting

    def setTimeCompleted(self, time_completed):
        self.__context["time_completed"] = time_completed

    #getters

    def getIdentifier(self):
        return int(self.__identifier)

    def getState(self):
        return self.__state

    def getPriority(self):
        return self.__priority
    
    def getPc(self):
        return self.__pc

    def getMemoryPointers(self):
        return self.__memory_pointers

    def getContextData(self):
        return self.__context_data

    def getIOStatusInfo(self):
        return self.__io_status_info

    def getContext(self):
        return self.__context
    
    #getters for the context dictionary
    def getCpuTimeCompleted(self):
        return int(self.__context["cpu_time_completed"])

    def getTimeEnteredToQueue(self):
        return int(self.__context["time_entered_to_queue"])

    def getTimeStartedOnCpu(self):
        return int(self.__context["time_started_on_cpu"])

    def getTimeSpentWaiting(self):
        return int(self.__context["time_spent_waiting"])

    def getTimeCompleted(self):
        return int(self.__context["time_completed"])
    
    def getCpuTimeToComplete(self):
        return int(self.__context["cpu_time_to_complete"])

    #output to string
    def toString(self):
        print( str(self.__identifier) + ", " + str(self.__state) + ", " + str(self.__priority) + ", " + str(self.__pc) + ", " + str(self.__memory_pointers) + ", " + str(self.__context_data) + ", " + str(self.__io_status_info) + ", " + str(self.__context) )

    def toDict(self):
        return {"identifier": self.__identifier,
                "state" : self.__state,
                "priority" : self.__priority,
                "pc" : self.__pc,
                "memory_pointers" : self.__memory_pointers,
                "context_data" : self.__context_data,
                "io_status_info" : self.__io_status_info,
                "context" : self.__context}