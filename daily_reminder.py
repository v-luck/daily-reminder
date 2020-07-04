import time
import datetime
from datetime import datetime
from datetime import date

#Month dictionary that can take a user number and convert it into a month
monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

#class for date and wait time
class date_class():
    def __init__(self, month, day, year, time):
        self.month = month
        self.day = day
        self.year = year
        self.time = time
        self.date = datetime.strptime(str(("{} {} {} {}".format(self.month, self.day, self.year, self.time))), '%b %d %Y %I:%M%p')
    def wait_time(self):
        self.time_difference= (self.date - datetime.now()).total_seconds()
        time.sleep(self.time_difference)
        print("RING RING ALARM BING")

#user input that will be used as parameters for the date class
user_month = monthDict[int(input("Insert month number:"))]
user_day = input("Insert a day:")
user_year = input("Insert a year or nothing to default to current year")
if not user_year:
    user_year = datetime.today().year
user_time = input("Insert a time. Make sure to include AM and PM")

#execution of parameters within the class
user_date = date_class(user_month, user_day, user_year, user_time)
user_date.wait_time()














