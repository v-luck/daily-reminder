import time
import datetime
from datetime import datetime
class date_class():
    def __init__(self, month, day, year, time):
        self.month = month
        self.day = day
        self.year = year
        self.time = time

user_input = "Jun 1 2005 1:33PM"
datetime_object = datetime.strptime(user_input, '%b %d %Y %I:%M%p')







print((datetime.now(tz=None)))
#datetime.strptime("09/19/18 3:30", "%)


