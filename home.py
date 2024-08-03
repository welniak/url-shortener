from flask import Flask, request

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