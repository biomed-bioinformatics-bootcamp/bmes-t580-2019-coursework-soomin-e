import os
import shutil
import platform
import subprocess

import requests


def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:  # Write in binary
        shutil.copyfileobj(data, fout)

def get_or_create_output_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path

def download_cats(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat ' + name)
        get_cat(folder, name)

    print("done.")
def display_cats(folder):
    # open folder
    print('Displaying cats in OS window.')
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())


print('-------------------------')
print('     LOL Cat Factory')
print('-------------------------')
print()

folder = get_or_create_output_folder()  # Creates Folder for Cat Images
download_cats(folder)
display_cats(folder)