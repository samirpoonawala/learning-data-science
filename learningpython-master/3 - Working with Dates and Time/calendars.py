# Example file for working with calendars

# import the calendar module
import calendar

# create the plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2018,5,0,0)
#print(str)

# create an html formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2018,1)
#print(st)

# loop over the days of a month
# zeros mean that the day of the week is in an overlapping month
# for i in c.itermonthdays(2018,8):
# 	print(i)


# the calendar module provides useful utilities for the given local
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
# 	print(name)

# for day in calendar.day_name:
# 	print(day)


# calculate days based on a rule
# for example, consider a team meeting on the first fri of each month
# to figure out what days that would be for each month, we can use:
print("Team meetings will be on: ")
for m in range(1,13):
	cal = calendar.monthcalendar(2018, m)
	weekone = cal[0]
	weektwo = cal[1]

	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		meetday = weektwo[calendar.FRIDAY]

	print("%10s %2d" % (calendar.month_name[m], meetday))