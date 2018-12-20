from math import ceil
import datetime
import os
import json

def week_of_month(data):
    """ Returns the week of the month for the specified date.
    """

    dt = datetime.datetime.now()

    MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_num = 7#dt.month
    month = MONTHS[month_num-1]

    day = 31 #dt.day

    month_data = data[month.upper()]

    while True:
        for week in month_data:
            for date in week['dates']:
                if day < int(date):
                    print("N/A")
                    return 0
                if int(date) == day:
                    print("we found today")
                    print(week['codes'])
                    return 0
        if month_num == 12:
            new_month = MONTHS[0]
            month_data = data[new_month.upper()]
        else:
            new_month = MONTHS[month_num+1]
            month_data = data[new_month.upper()]
    print(month_data)

    return 0
def get_schedule_times(codes):
    path = os.path.dirname(os.path.abspath(__file__))
    with open(f"{path}/schedules.json") as f:
        data = json.load(f)
    print(data['M'][0])
get_schedule_times('M')