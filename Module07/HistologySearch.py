import csv
from google_images_download import google_images_download

# Print Header
print('-----------------------')
print('   Histology Search')
print('-----------------------')
print()

terms = []
response = google_images_download.googleimagesdownload()

with open('searchterms.csv', 'r') as filename:
    data = csv.reader(filename)
    terms = list(data)

terms.pop(0)    # Removes the Header

for i in terms:
    keysearch = {'keywords': i[1], 'limit': '10', 'print_urls': True, 'prefix': i[0]}

    data = response.download(keysearch)
