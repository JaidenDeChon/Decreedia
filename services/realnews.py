# -*- coding: UTF-8 -*-


import feedparser


__program__ = "realnews.py"
__author__ = "Jaiden D. DeChon"
__copyright__ = "Copyright (C) 2017 Jaiden D. DeChon"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Jaiden D. DeChon"
__contact__ = "dechonjaiden@gmail.com"
__status__ = "Development"


url = "http://therealnews.com/rss/therealnews.rss"

posts= []

front_page = feedparser.parse(url)

def make_rss_dictionary():
    """ Grabs the RSS data and makes a dictionary out of the wanted information """

    print('*** Real News Network ***')
    print('Fetching Real News Network feed...')

    for article in front_page['entries']:
        posts.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
            "thumbnail": article.media_thumbnail[0]['url'],
        })

    print('Done\n')
    print('*** Finished with Real News Network ***\n\n')

make_rss_dictionary()

# for i in posts:
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
