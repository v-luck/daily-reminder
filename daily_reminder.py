import time
import datetime
from datetime import datetime
from datetime import date
class date_class():
    def __init__(self, month, day, year, time):
        self.month = month
        self.day = day
        self.year = year
        self.time = time
        self.date = datetime.strptime(str(("{} {} {} {}".format(self.month, self.day, self.year, self.time))), '%b %d %Y %I:%M%p')
monthDict={1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
user_month = monthDict[int(input("Insert month number:"))]
user_day = input("Insert a day:")
user_year = input("Insert a year or nothing to default to current year")
if not user_year:
    user_year = datetime.today().year
user_time = input("Insert a time. Make sure to include AM and PM")
user_date = date_class(user_month, user_day, user_year, user_time)

difference = (user_date.date - datetime.now()).total_seconds()
time.sleep(difference)
print("hello")













