
from bs4 import BeautifulSoup
import feedparser
import urllib.request

"""

To do:

- WOO HOO! This works just as it should.

- Next step is to append the thumbnails to their respective dictionaries when paired with the real program.

  - Perhaps this can be done by adding the thumbnail to the correct place in the dictionary during the first for loop

    - posts.append({"thumbnail": images}) where article.link == posts.link #(or posts.url?)

    - I'm hoping it can be done in one line, kind of like this ^^^

    - Must remember to add .join() method around it to make sure it doesn't go in as a list item instead of string
"""


# Grab all the XML from RSS feed
feed = feedparser.parse("http://www.aljazeera.com/xml/rss/all.xml")

# For storing links to thumbnails
thumbnails = []

# This will loop over every article link, find the main image, and add it to [thumbnails]
for article in feed["entries"]:
    html = urllib.request.urlopen(article.link)
    soup = BeautifulSoup(html, "html.parser")
    images = [hit['src'] for hit in soup.find_all("img", class_="article-main-img")]

    # .join is used while appending to [thumbnails]. This is because the line ABOVE returns lists instead of strings.
    thumbnails.append(''.join(([x.replace('') if x == None else x for x in images])))


# Replace the empty strings (which are where the image wasn't found) with default logo
thumbnails = ['http://www.aljazeera.com/mritems/assets/images/aj-logo-lg.png' if x=='' else x for x in thumbnails]

beginning_of_url = "http://www.aljazeera.com"

thumbnails = [beginning_of_url + i if not i.startswith("http") else i for i in thumbnails]

# Uncomment to view the links
# for i in thumbnails:
#     print(i)

thumbnails = ['http://www.aljazeera.com/mritems/assets/images/aj-logo-lg.png' if x['pic']=='' else x['pic'] for x in thumbnails]

