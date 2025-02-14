import argparse
from include import definitions
from include import jobs

# Create an argparse object
parser = argparse.ArgumentParser(description="Job scheduler simulator")
parser.add_argument("-I", "--input", type=str, help="Use a specific json job file, default is jobs.json")
parser.add_argument("-R", "--roundrobin", action="store_true", help="Use the round robin job scheduler")

# parse args
args = parser.parse_args()

file_input = "../res/jobs.json"

# Define file input
if args.input:
    file_input = args.input
if args.roundrobin:
    print("Round Robin enabled")
