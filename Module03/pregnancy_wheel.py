# Title Print
print('---------------------------------')
print('         Pregnancy Wheel')
print('---------------------------------')
print()

# Library Import
import datetime

# Local Functions

# Finding the lateste normal menstrual period
def get_lmp_from_patient():
    print("When was the patient's last normal menstrual cycle?")

    date_str = input('Format: [dd/mm/yyyy] \n')  # 05/06/19

    parts = date_str.split('/')
    if len(parts) != 3:
        print('Bad Date Found:', date_str)
        return get_lmp_from_patient()

    year = int(parts[2])
    month = int(parts[1])
    day = int(parts[0])

    lmp = datetime.date(year, month, day)

    return lmp

# Finding the distance between the two days
    # oDate is the original date
    # tDate is the target date
def dateDistance(oDate, tDate):
    this_year = datetime.date(tDate.year, oDate.month, oDate.day)

    dt = this_year - tDate
    return dt.days

# Printing out the expected due date information
def print_due_date_information(min_due_date, max_due_date, exp_due_date):
    print("Congrats! You are due", exp_due_date.strftime('%A, %b %d %Y!'))
    print('But it may be as early as', min_due_date.strftime('%m/%d/%Y.'))
    print('And it may be as late as', max_due_date.strftime('%m/%d/%Y.'))


# Getting Date Information
today = datetime.date.today()
lmp = get_lmp_from_patient()

# Estimating Gestation Age
gAge = dateDistance(today, lmp)
print()
print('Your estimate gestational age is %i days' % gAge)
print()

# Expected Due Date based on swedish study (281 +/- 13 days)
gest_length = datetime.timedelta(days = 281)
gest_std = datetime.timedelta(days = 13)

exp_due_date = lmp + gest_length
min_due_date = exp_due_date - gest_std
max_due_date = exp_due_date + gest_std

# Output Information
print_due_date_information(min_due_date, max_due_date, exp_due_date)