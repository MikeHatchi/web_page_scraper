#!/Users/Home/anaconda3/bin/python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import urlparse
import os


# function to (when content's been retrieved) store content at a specific
# directory with content's name.
def dl_yimg(web_adrs, file_path, file_name):
    full_path = file_path + file_name
    urllib.request.urlretrieve(web_adrs, full_path)
    print('done')


# Ask to user its web page for scraping
url = input('The URL please:')


# set of methods to retrieve specific content based on how the targeted
# web page has been structured.
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
gallery = soup.find(id='gallery')
img = gallery.find_all('img')
img2 = gallery.find_all('img')

path_scrap_dir = '/Users/Home/directory_to_store_the_retrieved_content'
split_scrap = path_scrap_dir + '/the_specific_folder_name/'

# loop for image download with title (zip here is what I'm found the more
# relevant to retrieve 2 different content trough the same tag.)
# pylint comment is specific to pylint bug in Atom 1.27.2
for link, item in zip(img, img2):
    image = link.get("src")
    # pylint: disable=no-member
    count = os.path.basename(image)
    file_name = item.get("title") + count + '.jpg'
    print(image)
    print(file_name)

    dl_yimg(image, split_scrap, file_name)
