from datetime import datetime
from json import loads

class NewsWork:
    def __init__(self, list):
        self.list = list

    def news_time(self)
        # fill random object because jinja starts index at 1
        how_long_ago = ['lowell help forum filler bot to help jinja yay']
        time_unit = ['lowell help forum filler bot to help jinja yay']
        # Get current Time
        now = datetime.now()

        # Code to display how long ago code was created
        for times in self.list:
            # Get time when post was created (datetime object)
            then = times.time_created
            # Calculate delta time (how much time between now and when post was created)
            delta = now - then
            # Get delta days (days from post creation)
            delta_days = delta.days
            # Get delta seconds (seconds from post creation)
            # datetime only has delta data on days, seconds, and micro seconds
            # Must multiply seconds to find minutes and hour
            delta_seconds = delta.seconds

            # If post was created over a day
            if delta_days != 0:
                # If post was created over a month
                if delta_days >= 30:
                    # If post was created over a year
                    if delta_days >= 365:
                        # set number shown as delta years
                        temp_time = delta_days // 365
                        time_ago = int(temp_time)
                        # If over 1 year use 'years' else just 'year'
                        if time_ago == 1:
                            time_measure = 'year'
                        else:
                            time_measure = 'years'
                    else:
                        # set number shown as delta months
                        temp_time = delta_days // 30
                        time_ago = int(temp_time)
                        # If over 1 month use 'months' else just 'month'
                        if time_ago == 1:
                            time_measure = 'month'
                        else:
                            time_measure = 'months'
                else:
                    # set number shown as delta days
                    time_ago = delta_days
                    # If over 1 day use 'days' else just 'day'
                    if delta_days == 1:
                        time_measure = 'day'
                    else:
                        time_measure = 'days'
            # Post was not created over a day ago
            else:
                # Check if post was created a minute or more ago
                if delta_seconds >= 60:
                    # Check if post was created a hour or more ago
                    if delta_seconds >= 3600:
                        # Set number shown as delta seconds divided by 3600(seconds in hour) and made into a integer
                        temp_time = delta_seconds // 3600
                        time_ago = int(temp_time)
                        # If over 1 hour use 'hours' else just 'hour'
                        if time_ago == 1:
                            time_measure = 'hour'
                        else:
                            time_measure = 'hours'
                    # Post was created minutes ago less than a hour
                    else:
                        # Set number shown as delta seconds divided by 60(seconds in minute) and made into a integer
                        temp_time = delta_seconds // 60
                        time_ago = int(temp_time)
                        # If over 1 minute use 'minutes' else just 'minute'
                        if time_ago == 1:
                            time_measure = 'minute'
                        else:
                            time_measure = 'minutes'
                # Post was created seconds ago less than a minute
                else:
                    # set number shown as delta seconds
                    time_ago = delta_seconds
                    # set time unit as seconds since the likely hood of seeing a post after just 1 second is near impossible
                    time_measure = 'seconds'
            how_long_ago.append(time_ago)
            time_unit.append(time_measure)

        return how_long_ago, time_unit

    def news_sort(self):
        news_data = {'news_data':{}}
        for number in len(self.list):
            if self.check_ten(number) == True:
                news_data['userdata'][str(number)] = {}
        for items in self.list:
            pass

    def check_ten(self, number):
        var_num = number % 10
        if var_num == 0:
            return True
        else:
            return False
