
# count = dict()
# fhandle = open('C:/Users/Adams/Desktop/PYTHON PRACTICE PROJECT/CODE SNIPPET/code3 PY4E\code3/words.txt')
# for file in fhandle:
#     word = file.rstrip().split()
#     for wd in word:
#         count[wd] = count.get(wd,0) + 1
# ls = list()
# lgcount = -1
# lgword = None
# for key, value in count.items():
#     # ls.append((value, key))
#     # ls.sort(reverse=True)
#     if value > lgcount:
#         lgcount = value
#         lgword = key
# print(lgword, lgcount)
# # for k, v in ls[:5]:
#   
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# ctx = ssl.create_default_context
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# fhandle = urllib.request.urlopen('http://www.dr-chuck.com')
# a = fhandle.read().decode()

# soup = BeautifulSoup(a, 'html.parser')
# tags = soup.find_all('a')
# print(tags)
# for tag in tags:
#     print(tag.get('href'))

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors for https
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

todo = list()
visited = list()
url = input('Enter - ')
todo.append(url)
count = int(input('How many to retrieve - '))

while len(todo) > 0 and count > 0 :
    print("====== To Retrieve:",count, "Queue Length:", len(todo))
    url = todo.pop()
    count = count - 1

    if (not url.startswith('http')):
        print("Skipping", url)
        continue

    if (url.find('facebook') > 0):
        continue

    if (url.find('linkedin') > 0):
        continue

    if (url in visited):
        print("Visited", url)
        continue

    print("===== Retrieving ", url)

    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print("*** Error in retrieval")
        continue

    soup = BeautifulSoup(html, 'html.parser')
    visited.append(url)

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        newurl = tag.get('href', None)
        if (newurl is not None):
            todo.append(newurl)