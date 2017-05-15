
# -*- coding: UTF-8 -*-

import feedparser
from bs4 import BeautifulSoup
import urllib.request

__program__ = "aljazeera.py"
__author__ = "Jaiden D. DeChon"
__copyright__ = "Copyright (C) 2017 Jaiden D. DeChon"
__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Jaiden D. DeChon"
__contact__ = "dechonjaiden@gmail.com"
__status__ = "Development"


domain = "http://www.aljazeera.com"
url = "http://www.aljazeera.com/xml/rss/all.xml"


def make_rss_dictionary():
    """ Grabs the RSS data and makes a dictionary out of the wanted information """
    print('*** Al Jazeera ***')
    print('\nFetching Al Jazeera feed...')

    feed = feedparser.parse(url)

    rss_dict = []

    for article in feed['entries']:
        rss_dict.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
        })

    print('Done\n')

    return rss_dict


def add_thumbnails():
    """ Assigns a suitable thumbnail to each article, since Al Jazeera RSS does not include thumbnails """
    print('Appending thumbnails, please wait...')

    for entry in posts:
        html = urllib.request.urlopen(entry['url'])
        soup = BeautifulSoup(html, "html.parser")

        def image():
            """ If you can find the image, complete the URL and use it for image source. If not, use default logo. """
            if [hit['src'] for hit in soup.find_all("img", class_="article-main-img")]:
                source = domain + (''.join([hit['src'] for hit in soup.find_all("img", class_="article-main-img")]))
            else:
                source = 'https://s-media-cache-ak0.pinimg.com/originals/40/07/7d/40077dab81aa75040734a3bb9003422f.jpg'
            return source

        entry.update({
            "thumbnail": (''.join(([x.replace('') if x is None else x for x in image()])))
        })

    print('Done\n')

    print('*** Finished with Al Jazeera ***\n\n')


posts = make_rss_dictionary()
add_thumbnails()


# Uncomment to print data
# for i in posts:
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
