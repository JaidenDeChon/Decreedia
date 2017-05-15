# -*- coding: UTF-8 -*-


import feedparser


__program__ = "independent.py"
__author__ = "Jaiden D. DeChon"
__copyright__ = "Copyright (C) 2017 Jaiden D. DeChon"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Jaiden D. DeChon"
__contact__ = "dechonjaiden@gmail.com"
__status__ = "Development"


# Does not contain front page data because Independent front page contains non-essential articles
# e.g. entertainment news, gossip, "Talking Points" (which contain opinions on social topics)


world_url = "http://www.independent.co.uk/news/world/rss"
uk_url = "http://www.independent.co.uk/news/uk/rss"
business_url = "http://www.independent.co.uk/news/business/rss"


world_feed = feedparser.parse(world_url)
uk_feed = feedparser.parse(uk_url)
business_feed = feedparser.parse(business_url)


world = []
uk = []
business = []


def make_dicts():
    """ Grabs the RSS data and makes a dictionary out of the wanted information """

    print('*** Independent ***')
    print('\nFetching Independent World feed...')

    for article in world_feed['entries']:
        world.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
            "thumbnail": article.media_content[0]['url'],
        })

    print(' Done\n')

    print('Fetching Independent UK feed...')

    for article in uk_feed['entries']:
        uk.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
            "thumbnail": article.media_content[0]['url'],
        })

    print('Done\n')

    print('Fetching Independent Business feed...')

    for article in business_feed['entries']:
        business.append({
            "title": article.title,
            "description": article.summary,
            "url": article.link,
            "thumbnail": article.media_content[0]['url'],
        })

    print('Done\n')

    print('*** Finished with Independent ***\n\n')

make_dicts()


# Uncomment to print data

# for i in world:
#     print("WORLD")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in uk:
#     print("UK")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
#
# print("\n \n \n \n")
#
# for i in business:
#     print("BUSINESS")
#     print(i['title'])
#     print(i['description'])
#     print(i['url'])
#     print(i['thumbnail'] + "\n")
