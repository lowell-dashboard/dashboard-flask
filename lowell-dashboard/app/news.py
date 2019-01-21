from datetime import datetime
from json import loads

class NewsWork:
    def __init__(self, list):
        self.list = list

    def news_sort(self):
        news_data = {'news_data':{}}
        list_length = int(len(self.list))
        count = 0
        for number in range(0, list_length):
            if self.check_ten(number) == True:
                count += 1
                news_data['news_data'][str(count)] = {'time_created_list':[],'time_measure':[],'new_post':[]}
        temp_news_data = self.time_sort(news_data)
        final_news_data = self.news_data_sort(temp_news_data)
        return final_news_data

    def time_sort(self, dic):
        # fill random object because jinja starts index at 1
        how_long_ago = ['lowell help forum filler bot to help jinja yay']
        time_unit = ['lowell help forum filler bot to help jinja yay']
        # Get current Time
        now = datetime.now()
        # Keeping dictionary count
        count = 1
        # Keeping Loop count
        loop_count = 0

        # Code to display how long ago code was created
        for times in self.list:
            loop_count += 1
            if self.check_ten(loop_count) == True:
                count += 1
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
            dic['news_data'][str(count)]['time_created_list'].append(time_ago)
            dic['news_data'][str(count)]['time_measure'].append(time_measure)

        return dic

    def news_data_sort(self, dic):
        # dictionary count
        count = 1
        # loop count
        loop_count = 0
        # loop for all items in list
        for news in self.list:
            # count loops
            loop_count += 1
            # loop looped multiple of 10
            if self.check_ten(loop_count) == True:
                # change data output to diffent page
                count += 1
            # add db object to proper lists
            dic['news_data'][str(count)]['new_post'].append(news)

        return dic

    def check_ten(self, number):
        var_num = number % 10
        if var_num == 0:
            return True
        else:
            return False
