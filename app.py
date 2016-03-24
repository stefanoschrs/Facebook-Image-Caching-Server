#!/usr/bin/env python
"""
Simple caching server for images retrieved from graph
"""

import urllib
from os import path
from flask import Flask, send_file

__author__ = "Stefanos Chrs"
__email__ = "stefanoschrs@hotmail.com"
__version__ = "1.0.0"
__status__ = "Production"
__license__ = "MIT"


IMAGES_DIR = './images'
TOKEN_LOCATION = 'access_token.txt'

app = Flask(__name__)

def fetch_image(page_id):
	urllib.urlretrieve('https://graph.facebook.com/' + page_id + '/picture?type=large& access_token=' + open(TOKEN_LOCATION, 'r').read(), IMAGES_DIR + '/' + page_id)

@app.route('/')
def index():
    return 'Facebook Image Caching API ' + __version__

@app.route('/image/<page_id>')
def image(page_id):
	if not path.isfile(IMAGES_DIR+'/'+page_id):
		fetch_image(page_id)
	return send_file(IMAGES_DIR+'/'+page_id)

if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')