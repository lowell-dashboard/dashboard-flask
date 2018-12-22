from math import ceil
import datetime
import os
import json

def find_week():
    path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{path}/result.json") as f:
        data = json.load(f)

    dt = datetime.datetime.now()

    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_num = dt.month
    month = MONTHS[month_num-1]

    day = 3 #dt.day

    month_data = data[month.upper()]

    while True:
        for week in month_data:
            for date in week['dates']:
                if day < int(date):
                    # print("N/A")
                    return []
                if int(date) == day:
                    # print("we found today")
                    # print(week['codes'])
                    return week
        if month_num == 12:
            new_month = MONTHS[0]
            month_data = data[new_month.upper()]
        else:
            new_month = MONTHS[month_num+1]
            month_data = data[new_month.upper()]
    return []
def week_of_month():
    """ Returns the week of the month for the specified date.
    """

    week_data = find_week()
    if len(week_data) == 0:
        return "00000"
    return week_data['codes']

def get_schedule_times(codes):
    path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{path}/schedules.json") as f:
        data = json.load(f)
    schedule_for_week = []
    for code in codes:
        try:
            schedule = data[code]
            schedule_for_week.append(schedule)
        except Exception as e:
            print(e)
    # print(schedule_for_week)
    # print(data['M'][0])
    return schedule_for_week

def get_week_events():
    week_data = find_week()
    if len(week_data) == 0:
        return "No message found"
    return week_data['events'] 