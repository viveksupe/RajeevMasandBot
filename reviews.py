import os
import re
import urllib2
from collections import OrderedDict
import requests

from bs4 import BeautifulSoup

review_page = {'Bollywood:\n': 'https://www.rajeevmasand.com/category/reviews/our-films/',
               'Hollywood:\n': 'https://www.rajeevmasand.com/category/reviews/their-films/'}
for page_to_scan in review_page:
    output = page_to_scan
    page = urllib2.urlopen(review_page[page_to_scan])
    soup = BeautifulSoup(page, 'html.parser')
    review_list = soup.find("div", {"class": "have-you-seen"})
    links_to_process = OrderedDict()
    for link in review_list.find_all('a', href=True):
        links_to_process[link.text] = link['href']

    for movie_name in links_to_process:
        page = urllib2.urlopen(links_to_process[movie_name])
        soup = BeautifulSoup(page, 'html.parser')
        for images in soup.find_all('img'):
            if re.match(r"<img alt=\"[0-6.]*\" src=\"/assets/images", str(images)):
                output += "--------------------------------------------------\n" + movie_name + "\n\tRating: " + images[
                    "alt"] + "\n--------------------------------------------------\n"

    r = requests.post(os.environ['SLACK_URL'],
                      data={'text': output})
    print r.text
