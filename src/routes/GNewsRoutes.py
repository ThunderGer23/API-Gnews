from flask import Blueprint, request, jsonify

import traceback

from src.utils.Logger import Logger
from src.utils.Security import Security
from src.services.GNewsService import GNewsService

main = Blueprint('articles', __name__)


@main.route('/')
def get_articles():
    """
    The function `get_articles()` retrieves articles from a news service and returns them as a JSON
    response, along with a success message, if the user has access. If the user does not have access, it
    returns an unauthorized response.
    :return: a JSON response. If the access token is verified, it returns a JSON object with the
    articles, a success message, and a success flag. If there are no articles, it returns a JSON object
    with a not found message and a success flag. If there is an exception, it returns a JSON object with
    an error message and a success flag. If the access token is not
    """
    has_access = Security.verify_token(request.headers)

    if has_access:
        try:
            articles = GNewsService.get_articles()
            if (len(articles) > 0):
                return jsonify({'articles': articles, 'message': "SUCCESS", 'success': True})
            else:
                return jsonify({'message': "NOTFOUND", 'success': True})
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

            return jsonify({'message': "ERROR", 'success': False})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401
