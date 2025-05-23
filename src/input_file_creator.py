import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

job_list = [
            {"identifier": 1, "state": "not_running", "priority": 0, "pc": 0, "memory_pointers": 0, "context_data": 0, "io_status_info": 0, "global_timer": 0,
                "context": {
                    "cpu_time_to_complete": 100, 
                    "cpu_time_completed": 0, 
                    "time_entered_to_queue": 0, 
                    "time_started_on_cpu": 0, 
                    "time_spent_waiting": 0, 
                    "time_completed": 0
                }
             },
             {"identifier": 2, "state": "not_running", "priority": 0, "pc": 0, "memory_pointers": 0, "context_data": 0, "io_status_info": 0, "global_timer": 0,
                "context": {
                    "cpu_time_to_complete": 300, 
                    "cpu_time_completed": 0, 
                    "time_entered_to_queue": 0, 
                    "time_started_on_cpu": 0, 
                    "time_spent_waiting": 0, 
                    "time_completed": 0
                }
             },
             {"identifier": 3, "state": "not_running", "priority": 0, "pc": 0, "memory_pointers": 0, "context_data": 0, "io_status_info": 0, "global_timer": 0,
                "context": {
                    "cpu_time_to_complete": 200,
                    "cpu_time_completed": 0,
                    "time_entered_to_queue": 0,
                    "time_started_on_cpu": 0,
                    "time_spent_waiting": 0,
                    "time_completed": 0
                }
             },
            {"identifier": 4, "state": "not_running", "priority": 0, "pc": 0, "memory_pointers": 0, "context_data": 0, "io_status_info": 0, "global_timer": 0,
                "context": {
                    "cpu_time_to_complete": 100,
                    "cpu_time_completed": 0,
                    "time_entered_to_queue": 0,
                    "time_started_on_cpu": 0,
                    "time_spent_waiting": 0,
                    "time_completed": 0
                }
            },
            {"identifier": 5, "state": "not_running", "priority": 0, "pc": 0, "memory_pointers": 0, "context_data": 0, "io_status_info": 0, "global_timer": 0,
                "context": {
                    "cpu_time_to_complete": 400,
                    "cpu_time_completed": 0,
                    "time_entered_to_queue": 0,
                    "time_started_on_cpu": 0,
                    "time_spent_waiting": 0,
                    "time_completed": 0
                }
            },
            ]

with open("jobs.json", "w") as file:
    json.dump(job_list, file, indent=4)