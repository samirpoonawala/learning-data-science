# Example file for working with timedelta objects

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
# print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is: " + str(now))

# print today's date one year from now
print("One year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In two days and three weeks it will be " + str(now + timedelta(days=2, weeks=3)))

# calculate the date one week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago it was: " + s)

# how many days until April fool's day?
today = date.today()
afd = date(today.year, 4,1 )

if afd < today:
	print("April fools day already went by %d days ago" % ((today-afd).days))
	afd = afd.replace(year=today.year + 1)

# now calculate the time until next April fool's day
time_to_afd = afd - today
print("It's just ", time_to_afd, "days until next April Fool's day")
