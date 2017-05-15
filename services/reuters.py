
# -*- coding: UTF-8 -*-


import feedparser


__program__ = "reuters.py"
__author__ = "Jaiden D. DeChon"
__copyright__ = "Copyright (C) 2017 Jaiden D. DeChon"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Jaiden D. DeChon"
__contact__ = "dechonjaiden@gmail.com"
__status__ = "Development"

""" 
 
 To Do: 
 
    - Reuters generally has a slideshow, video or (less commonly) a single image
    - Try to cover all those bases when searching for the image to use
 
"""


def world():
    # Grab the Reuters World News feed
    url = "http://feeds.reuters.com/Reuters/worldNews?format=xml"
    feed_data = feedparser.parse(url)
    return feed_data


def us():
    # Grab the Reuters US News feed
    url = "http://feeds.reuters.com/Reuters/domesticNews?format=xml"
    feed_data = feedparser.parse(url)
    return feed_data


def politics():
    # Grab the Grab the Reuters Politics feed
    url = "http://feeds.reuters.com/Reuters/PoliticsNews?format=xml"
    feed_data = feedparser.parse(url)
    return feed_data


def world_videos():
    # Grab the Reuters World News Videos feed
    url = "http://feeds.reuters.com/reuters/USVideoWorldNews?format=xml"
    feed_data = feedparser.parse(url)
    return feed_data

world()
us()
politics()
world_videos()
