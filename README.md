# Facebook Image Caching Server
Simple caching server for images retrieved from graph

Prerequisites
-
* `pip`
* `virtualenv`

Installation (recommended)
-
* Create the env `virtualenv --no-site-packages --distribute .env && source .env/bin/activate && pip install -r requirements.txt`
* Get a facebook access token (User token recommended since App token has some restrictions)
* Add the token to a file so you can easily change it `echo $ACCESS_TOKEN > access_token.txt`

Usage
-
* Start the server `python app.py`
* Visit `/image/<page_id>`
