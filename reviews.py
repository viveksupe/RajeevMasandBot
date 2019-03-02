import os
import pickle
import re
from collections import OrderedDict
import requests

from bs4 import BeautifulSoup

review_page = {'Bollywood:\n': 'https://www.rajeevmasand.com/category/reviews/our-films/',
               'Hollywood:\n': 'https://www.rajeevmasand.com/category/reviews/their-films/'}
FILE_NAME = '/usr/src/app/state.pkl'
state_content = None

try:
    pkl_file = open(FILE_NAME, 'rb')
    state_content = pickle.load(pkl_file)
    pkl_file.close()
except (IOError, EOFError):
    # If not exists, create the file
    pkl_file = open(FILE_NAME, 'wb+')
    pickle.dump(set(), pkl_file)
    pkl_file.close()

state_set = set() if state_content is None else state_content
current_state_set = set()

for page_to_scan in review_page:
    output = page_to_scan
    page = requests.get(review_page[page_to_scan])
    soup = BeautifulSoup(page.content, 'html.parser')
    review_list = soup.find("div", {"class": "have-you-seen"})
    links_to_process = OrderedDict()
    for link in review_list.find_all('a', href=True):
        links_to_process[link.text] = link['href']

    for movie_name in links_to_process:
        page = requests.get(links_to_process[movie_name])
        soup = BeautifulSoup(page.content, 'html.parser')
        for images in soup.find_all('img'):
            if re.match(r"<img alt=\"[0-6.]*\" src=\"/assets/images", str(images)):
                current_state_set.add(movie_name)
                if movie_name not in state_set:
                    output += "--------------------------------------------------\n" + movie_name + "\n\tRating: " + \
                              images["alt"] + "\n--------------------------------------------------\n"
                state_set.add(movie_name)
    if output is page_to_scan:
        output += "--------------------------------------------------\nNo New " \
                  "Reviews\n--------------------------------------------------\n "
    r = requests.post(os.environ['SLACK_URL'],
                      data={'text': output})
    print(r.text)

# Discard Old Entries
state_set = state_set.union(current_state_set)

output = open(FILE_NAME, 'wb')
pickle.dump(state_set, output)
output.close()
