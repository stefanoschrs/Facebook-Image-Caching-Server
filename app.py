#!/usr/bin/env python
"""
Simple caching server for images retrieved from graph
"""

import urllib
import re
from os import path
from flask import Flask, send_file, request

__author__ = "Stefanos Chrs"
__email__ = "stefanoschrs@hotmail.com"
__version__ = "1.1.0"
__status__ = "Production"
__license__ = "MIT"


IMAGES_DIR = './static/images'
# TOKEN_LOCATION = 'access_token.txt'

app = Flask(__name__, static_url_path='')

def fetch_image(page_id):
	# For some reason when using the access token the user profile picture is the default
	# urllib.urlretrieve('https://graph.facebook.com/' + page_id + '/picture?type=large& access_token=' + open(TOKEN_LOCATION, 'r').read(), IMAGES_DIR + '/' + page_id)
	urllib.urlretrieve('https://graph.facebook.com/' + page_id + '/picture?type=large', IMAGES_DIR + '/' + page_id)

@app.route('/')
def index():
    return 'Facebook Image Caching API ' + __version__

@app.errorhandler(404)
def page_not_found(e):
	if '/images/' in request.url:
		page_id = request.url.split('/')[-1]
		p = re.compile('^[0-9]+$')
		if p.match(page_id):
			fetch_image(page_id)
			return send_file(IMAGES_DIR+'/'+page_id)
		else:
			return 'Wrong Facebook ID'
	return 'Page not found'

if __name__ == '__main__': 
	app.run(debug=False, host='0.0.0.0')