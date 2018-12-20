from .make_schedule import schedule
import json
import os

path = os.path.dirname(os.path.abspath(__file__))

def update_schedule():
	schedule.main()
	with open(f'{path}/result.json', 'r') as f:
		parsed = json.load(f)
	parsed

def retrieve_schedule():
	with open(f'{path}/result.json', 'r') as f:
		parsed = json.load(f)
	return parsed
