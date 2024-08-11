from flask import request
from app import app
from app.logger import logger
from app.url_validator import is_valid_url
from app.url_processor import create_and_store_hash

@app.before_request
def log_request_info():
    logger.info('Headers: %s', request.headers)
    logger.info('Body: %s', request.get_data())

@app.route('/', methods=['POST'])
def shorten_url():
    content = request.json
    # Extract the url from the request
    url = content.get('url')
    if url is None:
        return 'No URL provided', 400
    elif not is_valid_url(url):
        return 'The provided URL is not valid. Please provide a URL in the format: http://www.example.com', 400
    else:
        url_hash = create_and_store_hash(url)
        return 'Hash: ' + url_hash, 200
