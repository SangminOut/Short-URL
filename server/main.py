from flask import Flask, request, redirect, Response
from server.model import save_url, get_url

app: Flask = Flask(__name__)


@app.route('/', methods=['POST'])
def post() -> Response:
    original_url = request.json['url']

    url_key = save_url(original_url)

    return Response('http://localhost/' + url_key, 201)


@app.route('/<key>', methods=['GET'])
def get(key) -> Response:
    url = get_url(key)

    if url is None:
        return Response('', 204)
    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 80)