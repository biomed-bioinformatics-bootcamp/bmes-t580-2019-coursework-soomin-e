# Title Print
print('---------------------------------')
print('           Birthday App')
print('---------------------------------')
print()

# Library Import
import datetime

# Local Functions
def dateDistance(oDate, tDate):
    this_year = datetime.date(tDate.year, oDate.month, oDate.day)

    dt = this_year - tDate
    return dt.days

# Getting User Birthday Information
year = int(input('What year were you born [YYYY]? '))
month = int(input('What month were you born [MM]? '))
day = int(input('What day were you born [DD]? '))

bday = datetime.date(year, month, day)
today = datetime.date.today()

numDays = dateDistance(bday, today)

if numDays < 0:
    print('Your birthday was %i day(s) ago from today!' % numDays)
elif numDays > 0:
    print('Your birthday is in %i day(s) from today!' % numDays)
else:
    print('Happy birthday!!')