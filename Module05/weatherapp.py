# Library Imports
import requests
import bs4

# Printing Header
print('-------------------------')
print('         Weather App')
print('-------------------------')
print()

# Function Definitions
def get_html_from_web(zip):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zip)
    response = requests.get(url)

    return response.text # Returning HTML

def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text

def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()

def get_weather_from_html(html):

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(condition, temp, scale, loc)
    # return condition, temp, scale, loc
    report = (loc, temp, scale, condition)
    return report

# Getting User Input
zip = input('Enter you zipcode (e.g. 19104): ')

html = get_html_from_web(zip)
fReport = get_weather_from_html(html)

print('The temp in {} is {} {} and {}'.format(
        fReport[0],
        fReport[1],
        fReport[2],
        fReport[3]
    ))