from flask import Flask, request
import logging

app = Flask(__name__)
app.debug = True

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
    
# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler and set level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to console handler
console_handler.setFormatter(formatter)

# Add console handler to logger
logger.addHandler(console_handler)

@app.before_request
def log_request_info():
    logger.info('Headers: %s', request.headers)
    logger.info('Body: %s', request.get_data())