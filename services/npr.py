
# -*- coding: UTF-8 -*-


import feedparser
from bs4 import BeautifulSoup
import urllib.request

__program__ = "npr.py"
__author__ = "Jaiden D. DeChon"
__copyright__ = "Copyright (C) 2017 Jaiden D. DeChon"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Jaiden D. DeChon"
__contact__ = "dechonjaiden@gmail.com"
__status__ = "Development"


front_url = "http://www.npr.org/rss/rss.php"
world_url = "http://www.npr.org/rss/rss.php?id=1004"
us_url = "http://www.npr.org/rss/rss.php?id=1003"
politics_url = "http://www.npr.org/rss/rss.php?id=1014"
education_url = "http://www.npr.org/rss/rss.php?id=311911180"


front_feed = feedparser.parse(front_url)
world_feed = feedparser.parse(world_url)
us_feed = feedparser.parse(us_url)
politics_feed = feedparser.parse(politics_url)
education_feed = feedparser.parse(education_url)

front = []
world = []
us = []
politics = []
education = []


def make_dicts():
    """ Grabs the RSS data and makes a dictionary out of the wanted information """

    print('*** NPR ***')
    print('Fetching NPR Front Page feed...')

    for article in front_feed['entries']:
        front.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')

    print('Fetching NPR World feed...')

    for article in world_feed['entries']:
        world.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')

    print('Fetching NPR US feed...')

    for article in us_feed['entries']:
        us.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')
    print('Fetching NPR Politics feed...')

    for article in politics_feed['entries']:
        politics.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')
    print('Fetching NPR Education feed...')

    for article in education_feed['entries']:
        education.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')


def add_thumbnails():
    """ Assigns a suitable thumbnail to each article """
    print('Appending NPR Front thumbnails...')

    for entry in front:

        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="img lazyOnLoad")]:
                pics = [x['src'] for x in soup.find_all("img", class_="img lazyOnLoad")]
                source = max(pics, key=len)
            else:
                source = 'http://media.npr.org/chrome_svg/npr-logo-color.svg'
            return source

        entry.update({
            "thumbnail" : (''.join(([x.replace('') if x == None else x for x in image()])))
        })

    print('Done\n')

    print('Appending NPR World thumbnails...')

    for entry in world:

        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="img lazyOnLoad")]:
                pics = [x['src'] for x in soup.find_all("img", class_="img lazyOnLoad")]
                source = max(pics, key=len)
            else:
                source = 'http://media.npr.org/chrome_svg/npr-logo-color.svg'
            return source

        entry.update({
            "thumbnail" : (''.join(([x.replace('') if x == None else x for x in image()])))
        })

    print('Done\n')

    print('Appending NPR US thumbnails...')

    for entry in us:

        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="img lazyOnLoad")]:
                pics = [x['src'] for x in soup.find_all("img", class_="img lazyOnLoad")]
                source = max(pics, key=len)
            else:
                source = 'http://media.npr.org/chrome_svg/npr-logo-color.svg'
            return source

        entry.update({
            "thumbnail" : (''.join(([x.replace('') if x == None else x for x in image()])))
        })

    print('Done\n')

    print('Appending NPR Politics thumbnails...')

    for entry in politics:

        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="img lazyOnLoad")]:
                pics = [x['src'] for x in soup.find_all("img", class_="img lazyOnLoad")]
                source = max(pics, key=len)
            else:
                source = 'http://media.npr.org/chrome_svg/npr-logo-color.svg'
            return source

        entry.update({
            "thumbnail" : (''.join(([x.replace('') if x == None else x for x in image()])))
        })

    print('Done\n')

    print('Appending NPR Education thumbnails...')

    for entry in education:

        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="img lazyOnLoad")]:
                pics = [x['src'] for x in soup.find_all("img", class_="img lazyOnLoad")]
                source = max(pics, key=len)
            else:
                source = 'http://media.npr.org/chrome_svg/npr-logo-color.svg'
            return source

        entry.update({
            "thumbnail" : (''.join(([x.replace('') if x == None else x for x in image()])))
        })

    print('Done\n')

    print('*** Finished with NPR ***\n\n')


make_dicts()
add_thumbnails()

# Uncomment to print data

# for i in front:
#     print("WORLD")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in world:
#     print("UK")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in us:
#     print("US")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in politics:
#     print("POLITICS")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in education:
#     print("EDUCATION")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
