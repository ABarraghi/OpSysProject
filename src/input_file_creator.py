import json

job_list = [{"job_number": 1, "time_to_complete": 100, "time_completed": 0},
             {"job_number": 2, "time_to_complete": 300, "time_completed": 0}]

with open("jobs.json", "w") as file:
    json.dump(job_list, file, indent=4)