from flask import Blueprint, request, jsonify

import traceback

from src.utils.Logger import Logger
from src.models.UserModel import User
from src.utils.Security import Security
from src.services.AuthService import AuthService

main = Blueprint('auth_blueprint', __name__)

@main.route('/', methods=['POST'])
def login():
    """
    The login function takes a username and password from a JSON request, attempts to authenticate the
    user, and returns a token if successful or an error message if unsuccessful.
    :return: a JSON response. If the user is authenticated successfully, it returns a JSON object with
    the keys 'success' and 'token'. If the user is not authenticated, it returns a JSON object with the
    key 'message' and a value of 'Unauthorized'. If an exception occurs, it returns a JSON object with
    the keys 'message' and 'success', both having values related to
    """
    try:
        username = request.json['username']
        password = request.json['password']

        _user = User(0, username, password, None)
        authenticated_user = AuthService.login_user(_user)

        if (authenticated_user != None):
            encoded_token = Security.generate_token(authenticated_user)
            return jsonify({'success': True, 'token': encoded_token})
        else:
            response = jsonify({'message': 'Unauthorized'})
            return response, 401
    except Exception as ex:
        Logger.add_to_log("error", str(ex))
        Logger.add_to_log("error", traceback.format_exc())

        return jsonify({'message': "ERROR", 'success': False})