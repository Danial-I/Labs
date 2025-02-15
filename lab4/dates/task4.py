from datetime import datetime,timedelta
import math
day1=input()
day2=input()
date_format = "%Y-%m-%d %H:%M:%S"
d1 = datetime.strptime(day1, date_format)
d2 = datetime.strptime(day2, date_format)
difference = abs((d2 - d1).total_seconds())
print (f"difference between {day1} and {day2} is {difference}")