from decouple import config

import datetime
import jwt
import pytz
import traceback

from src.utils.Logger import Logger


# The Security class is a placeholder for implementing security-related functionality.
class Security():

    secret = config('JWT_KEY')
    tz = pytz.timezone("America/Mexico_City")
    expected_keys = ['iat', 'exp', 'username', 'fullname']

    @classmethod
    def generate_token(cls, authenticated_user):
        """
        The function generates a token using the JWT library with an expiration time of 10 minutes and
        includes the username and fullname of the authenticated user.
        
        :param cls: The parameter `cls` is a reference to the class itself. It is commonly used in class
        methods to access class-level variables or methods
        :param authenticated_user: The authenticated_user parameter is an object representing the user
        who has been successfully authenticated. It should have properties such as username and
        fullname, which will be used to generate the token
        :return: a JSON Web Token (JWT) encoded with the given payload, secret, and algorithm.
        """
        try:
            payload = {
                'iat': datetime.datetime.now(tz=cls.tz),
                'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=10),
                'username': authenticated_user.username,
                'fullname': authenticated_user.fullname,
            }
            return jwt.encode(payload, cls.secret, algorithm="HS256")
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())

    @classmethod
    def verify_token(cls, headers):
        """
        The function `verify_token` checks if a token in the headers is valid by decoding it and
        verifying its signature.
        
        :param cls: The parameter `cls` is a reference to the class itself. It is commonly used in class
        methods to access class-level variables and methods
        :param headers: The `headers` parameter is a dictionary that contains the HTTP headers of a
        request. It is used to extract the 'Authorization' header, which typically contains a token for
        authentication purposes
        :return: a boolean value. It returns True if the token is valid and contains all the expected
        keys, and False otherwise.
        """
        try:
            if 'Authorization' in headers.keys():
                authorization = headers['Authorization']
                encoded_token = authorization.split(" ")[1]
                if ((len(encoded_token) > 0) and (encoded_token.count('.') == 2)):
                    try:
                        payload = jwt.decode(encoded_token, cls.secret, algorithms=["HS256"])
                        return True if all(key in payload for key in cls.expected_keys) else False
                    except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
                        return False

            return False
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
