from make_schedule import schedule
import json

def update_schedule():
	schedule.main()
	with open('result.json', 'r') as f:
		parsed = json.load(f)
	print(parsed)