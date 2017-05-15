
from flask import Flask
from flask import render_template
import jinja2
import aljazeera
import independent
import npr
import realnews


# Stored as variable so it can be called later without exceeding PEP8 line length-limit (see 'app.jinja-loader' below)
path_to_jinja_templates = 'C:/Users/jaide/OneDrive/Documents/Pro/Web Development/Headliner/templates'


# Create lists to house the content for all feeds. This is done so each feed process doesn't run multiple times.
# This method saves literally minutes of load time every time it runs. Outside Python files are executed every time \
# they're called, so doing this allows us to run each once then call on it when needed.
aljazeera_list = []

independent_world_list = []
independent_uk_list = []
independent_business_list = []

npr_front_list = []
npr_world_list = []
npr_us_list = []
npr_politics_list = []
npr_education_list = []

realnews_list = []


def make_aljazeera_list():
    """ Append Aljazeera contents to the list we created before """
    for article in aljazeera.posts:
        aljazeera_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })


def make_independent_lists():
    """ Append Independent contents to the lists we created before """
    for article in independent.world:
        independent_world_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in independent.uk:
        independent_uk_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in independent.business:
        independent_business_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })


def make_npr_lists():
    """ Append NPR contents to the lists we created before """
    for article in npr.front:
        npr_front_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in npr.world:
        npr_world_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in npr.us:
        npr_us_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in npr.politics:
        npr_politics_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })

    for article in npr.education:
        npr_education_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })


def make_realnews_list():
    """ Append RealNews contents to list we created before """
    for article in realnews.posts:
        realnews_list.append({
            "title": article['title'],
            "description": article['description'],
            "url": article['url'],
            "thumbnail": article['thumbnail']
        })


# Flask app setup
app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.jinja_loader = jinja2.FileSystemLoader(path_to_jinja_templates)


@app.route('/')
def make_cards():
    """ Creates the HTML using the template provided and the list contents """
    with app.app_context():
        return render_template('homepage.html',
                               aljazeera=aljazeera_list,

                               independent_world=independent_world_list,
                               independent_uk=independent_uk_list,
                               independent_business=independent_business_list,

                               npr_front=npr_front_list,
                               npr_world=npr_world_list,
                               npr_us=npr_us_list,
                               npr_politics=npr_politics_list,
                               npr_education=npr_education_list,

                               realnews=realnews_list,

                               font_url="https://fonts.googleapis.com/css?family=Roboto+Condensed",
                               mdl_js="https://code.getmdl.io/1.3.0/material.min.js")


# Create the lists to be fed to Flask app
make_aljazeera_list()
make_independent_lists()
make_npr_lists()
make_realnews_list()

make_cards()


# Keep this at the end or will have resulting 404
app.run(debug=True, use_reloader=False)


# In case services cannot be imported, import sys and use this to update the path:
# sys.path.append('C:/Path/To/Services/Folder')
