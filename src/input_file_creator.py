import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

job_list = [{"job_number": 1, "time_to_complete": 100, "time_completed": 0},
             {"job_number": 2, "time_to_complete": 300, "time_completed": 0},
             {"job_number": 3, "time_to_complete": 400, "time_completed": 0}]

with open("jobs.json", "w") as file:
    json.dump(job_list, file, indent=4)