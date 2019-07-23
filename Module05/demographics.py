# Library Imports
import csv
import os

def print_header():
    print('---------------------------------')
    print('       Process Demographics')
    print('---------------------------------')
    print()

def get_filename():

    # Initializes the variable
    filename = None

    # User Validation of the File
    while filename is None:

        filename = input('What is the /path/to/the/file? ')

        # Check if the filename exists.
        if not os.path.exists(filename):
            print('That file could not be found. Try again.')
            filename = None

    return filename

# Main File
print_header()
filename = get_filename()

# User Parameters
# User Input Validation
while True:
    try:
        sex = input('What is the target sex? (Male/Female/Both) ')
        minAge = int(input('What is the min age? (Enter a number) '))
        maxAge = int(input('What is the max age? (Enter a number) '))
        minInfection = int(input('What is the min infection length? (Enter a number) '))
        maxInfection = int(input('What is the max infection length? (Enter a number) '))
        therapy = input('Should the patients be on therapy? (Yes/No) ')
        coinfection = input('Should the patients have a coinfection? (Yes/No) ')
    except ValueError:
        print('Values are not correct. Please try again.')
        continue

    if sex not in 'MaleFemaleBoth' or therapy not in 'YesNo' or coinfection not in 'YesNo':
        print('Values are not correct. Please try again.')
        continue
    else:
        break

# Open file and start reader
with open(filename) as handle:
    reader = csv.DictReader(handle)
    pat_num = 0
    viablePat = []

    #Examines each row
    for row in reader:
        pat_sex =  row['SEX']
        pat_age = int(row['AGE'])
        pat_infection = int(row['INFECTION_LENGTH'])
        pat_therapy = row['ON_THERAPY']
        pat_coinfection = row['COINFECTION']

        # Separate out the long logic for clarity
        match_age = (pat_age > minAge) and (pat_age < maxAge)
        match_infection = (pat_infection >  minInfection) and (pat_infection < maxInfection)


        #Counting
        if match_age:
            if match_infection:
                if pat_sex == sex:
                    if pat_therapy == therapy:
                        if pat_coinfection == coinfection:
                            pat_num += 1
                            viablePat.append(row)

# Prints the Results
print('Based on the following criteria:')
print(' - Age: [%i, %i]' % (minAge, maxAge))
print(' - Length of infection: [%i, %i]' %(minInfection, maxInfection))
print(' - Sex: %s' % sex)
print(' - On Therapy: %s' % therapy)
print(' - Coinfection: %s' % coinfection)

print('There are %i eligible patients' % pat_num)

# Writing File
with open('ViablePatents.txt', 'w') as f:
    for item in viablePat:
        f.write("%s\n" % item)