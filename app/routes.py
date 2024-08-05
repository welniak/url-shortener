from flask import request
from app import app
from app.logger import logger
from app.url_validator import is_valid_url

@app.before_request
def log_request_info():
    logger.info('Headers: %s', request.headers)
    logger.info('Body: %s', request.get_data())

@app.route('/', methods=['POST'])
def shorten_url():
    content = request.json
    # Extract the url from the request
    url = content.get('url')
    print(url)
    if url is None:
        return 'No URL provided', 400
    elif not is_valid_url(url):
        return 'The provided URL is not valid', 400
    else:
        return '', 200
