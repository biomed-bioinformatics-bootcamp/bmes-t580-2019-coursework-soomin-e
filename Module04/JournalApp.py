# Print Introduction App
print('----------------------------------------')
print('          Personal Journal App')
print('________________________________________')

# Files and Functions Imports
import csv
import os

# Defining the Different Functions For Each Command
# List
def listJournal():
    entry = 1
    print()

    for i in journal:
        print(str(entry) + '.' + ' ', i)
        entry += 1
# Add
def addJournal():
    print()

    newEntry = input('Enter your next journal entry:\n')
    newEntry = newEntry + '\n'
    fid = open('ExampleJournal.txt', 'a')
    fid.write(newEntry)
    fid.close()


# Exit
def exitJournal():
    print()
    print('...saving to ExampleJournal.txt...')
    print('Save Complete')

# Opening File
def loadJournal():
    count = 0
    journal = []

    with open('ExampleJournal.txt') as fid:
        for line in fid.readlines():
            count += 1
            if line.rstrip() != '':
                journal.append(line.rstrip())

    return (journal, fid)


# Define Beginning Values
uCommand = ''
journal, fid = loadJournal()

print('...Loading journal from:', os.getcwd(), '...')
print('...Loading', len(journal), 'entries...')


while uCommand != 'x':
    # Getting the User Input
    journal, fid = loadJournal()
    uCommand = input('What do you want to do? [L]ist, [A]dd, or E[x]it? ').lower()

    if uCommand == 'l':         # List function
        listJournal()
    elif uCommand == 'a':       # Add function
        addJournal()
    elif uCommand == 'x':       # Exit function
        exitJournal()
    else:                       # Error Case
        print('Invalid Entry. Please try again or enter "x" to exit.')

    print('')
