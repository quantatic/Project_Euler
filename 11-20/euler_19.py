import time
startTime = time.clock()
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#1 is a monday, 7 is a sunday, etc.
weekday = 1
year = 1901
month = 1
monthDay = 1
total = 0
while year < 2001:
    if weekday == 7 and monthDay == 1:
        total += 1
        print("day", weekday, "monthDay", monthDay, "month", month, "year", year)
    if year % 4 == 0:
        months[1] = 29
    elif not months[1] == 28:
        months[1] = 28
    if weekday == 7:
        weekday = 1
    else:
        weekday += 1
    if monthDay >= months[month - 1]:
        month += 1
        monthDay = 1
    else:
        monthDay += 1
    if month > 12:
        month = 1
        year += 1
print("--- answer: %s ---" % total)
print("--- %s seconds ---" % (time.clock() - startTime))

