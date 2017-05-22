def isLeapYear(year):
    if year %400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
    
def daysInMonth(year, month):
    if month in (1,3,5,7,8,10,12):
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
        else:
            return 28
    return 30

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day < daysInMonth(year,month):
        return year, month, day +1
    if month < 12:
        return year, month + 1, 1
    else:
        return year +1, 1, 1
    
def dateIsBefore(year1, month1, day1, year2, month2, day2):

    assert not (year2,month2,day2,year1,month1,day1)
    if year1<year2:
        return True
    if year1 == year2:
        if month1<month2:
            return True
    if month1== month2:
        return day1<day2
    return False

def test():
    assert dateIsBefore (2013, 1, 1, 2013, 1,1) ==0
    assert dateIsBefore (2013, 1, 1, 2013, 1,2) ==1
    assert nextDay(2012,1,2) == (2012,1,3)
    assert nextDay (2013,4,30) == (2013,5,1)
    assert nextDay  (2013,12,30) == (2014,1,1)
    assert dateIsBefore(2012,1,1,2013,1,1) == 365

    
    assert dateIsBefore(2013,1,1,2014,1,1) == 365
print(")
