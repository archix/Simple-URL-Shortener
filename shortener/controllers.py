from flask import Blueprint, request, Response, redirect, json, current_app

from shortener.models import ShortUrl

shortener = Blueprint('shortener', __name__)


@shortener.route('/shorten', strict_slashes=False, methods=['POST'])
def shorten():
    data = request.get_json(force=True)
    response = {
        'original_link': data['url'],
        'short_link': ShortUrl.create_entry(data['url']).full_short_url
    }
    return Response(json.dumps(response),
                    status=200, mimetype='application/json')


@shortener.route('/<short>', methods=['GET'])
def visit(short):
    """Fixme This should be done in the function itself,
        with custom exceptions, etc.
    """
    if set(short).intersection(current_app.config['EXCLUDED_CHARACTERS']) > 0:
        return Response(
            status=400,
            response={'message': 'Invalid character(s) in url short code'},
            mimetype='application/json')
    url_object = ShortUrl.find_by_short_key(short)
    if url_object:
        return redirect(url_object.original_url, code=301)
    else:
        return Response(status=404, mimetype='application/json')
