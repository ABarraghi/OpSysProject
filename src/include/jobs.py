# create a common class object for jobs

class Job:
    def __init__(self, identifier, state, priority, pc, memory_pointers, context_data, io_status_info, context):
        self.__identifier = identifier
        self.__state = state
        self.__priority = priority
        self.__pc = pc
        self.__memory_pointers = memory_pointers
        self.__context_data = context_data
        self.__io_status_info = io_status_info
        self.__context = context

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

    #getters

    def getIdentifier(self):
        return self.__identifier

    def getState(self):
        return self.state

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