from math import ceil
import datetime
import os
import json
from calendar import monthrange

class ScheduleService(object):

    def __init__(self):
        self.dt = datetime.datetime.now()
        self.weeknum = datetime.datetime.today().weekday()
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    def find_week(self):
        with open(f"{self.path}/result.json") as f:
            data = json.load(f)

        day, month_num = self.handle_weekends(self.dt.day, self.dt.year, self.dt.month)

        month = self.MONTHS[month_num-1]
        month_data = data[month.upper()]
        # print(month_data)
        # print(month)
        while True:
            count = 0
            for week in month_data:
                for date in week['dates']:
                    if count >= 4:
                        # print("N/A")
                        return []
                    if int(date) == day:
                        # print("we found today")
                        # print(week['codes'])
                        return week
                count += 1
            if month_num == 12:
                new_month = self.MONTHS[0]
                month_data = data[new_month.upper()]
            else:
                new_month = self.MONTHS[month_num+1]
                month_data = data[new_month.upper()]
        return []

    def week_of_month(self):
        """ Returns the week of the month for the specified date.
        """

        week_data = self.find_week()
        if len(week_data) == 0:
            return "00000"
        print(week_data['codes'])
        print(week_data['dates'])
        return week_data['codes']

    def get_schedule_times(self, codes):
        with open(f"{self.path}/schedules.json") as f:
            data = json.load(f)
        schedule_for_week = []
        for code in codes:
            try:
                schedule = data[code]
                schedule_for_week.append(schedule)
            except Exception as e:
                # print(e)
                schedule_for_week.append(data["NotAvailable"])
        # print(schedule_for_week)
        # print(data['M'][0])
        return schedule_for_week

    def get_week_events(self):
        week_data = self.find_week()
        if len(week_data) == 0:
            return "No message found"
        return week_data['events']

    def handle_weekends(self, date, year, month):
        if self.weeknum < 5:
            return date, month
        elif self.weeknum == 5:
            # if it is the weekend show the schedule for upcoming week
            m, d = monthrange(year, month)
            if(date == d):
                return 2, month + 1
            return date + 2, month
        elif self.weeknum == 6:
            # if it is the weekend show the schedule for upcoming week
            m, d = monthrange(year, month)
            if(date == d):
                # print("something")
                return 1, month + 1
            return date + 1, month
