# Print Introduction App
print('----------------------------------------')
print('          Personal Journal App')
print('________________________________________')

# Files and Functions Imports
import journal

# Defining the Different Functions For Each Command
# List
def listJournal():


# Add
def addJournal():

# Exit
def exitJournal():

# Define Beginning Values
uCommand = ''


while uCommand != 'x':
    # Getting the User Input
    uCommand = input('What do you want to do? [L]ist, [A]dd, or E[x]it?').lower()

    if uCommand == 'l':         # List function
        listJournal()
    elif uCommand == 'a':       # Add function
        addJournal()
    elif uCommand == 'x':       # Exit function
        exitJournal()
    else:                       # Error Case
        print('Invalid Entry. Please try again or enter "x" to exit.')

    print('')
