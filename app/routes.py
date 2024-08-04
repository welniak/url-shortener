from flask import request
from app import app
from app.logger import logger

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
    else:
        return '', 200
