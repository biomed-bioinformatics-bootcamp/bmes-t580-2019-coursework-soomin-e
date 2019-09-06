# Library Imports
import os
import collections

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

# Function Definition

def search_folders(folder, text):
    files = os.listdir(folder)

    for item in files:
        full_file = os.path.join(folder, item)

        if os.path.isdir(full_file):
            yield from search_folders(full_file, text)
        else:
            yield from search_file(full_file, text)

def search_file(filename, text):
    with open(filename, encoding="utf8", errors='ignore') as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                m = SearchResult(line=line_num, file=filename, text=line)
                yield m

# Print Header
print('-----------------------')
print('    File Search App')
print('-----------------------')

# Input
uPath = input('What directory do you want to search? ')       # Identify the directory
folder = os.path.abspath(uPath)

print()

uString = input('What string are you looking for? ')           # Identify the desired string
text = uString.lower()

# File Search
matches = search_folders(folder, text)
print(matches)
match_count = 0

for m in matches:
    print(m)
    match_count += 1

print('%i total matches.' % match_count)
print('End of Search')
