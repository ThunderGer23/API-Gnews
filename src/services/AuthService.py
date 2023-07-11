import traceback

from src.database.db import get_connection
from src.utils.Logger import Logger
from src.models.UserModel import User


# The AuthService class is responsible for handling authentication and authorization functionality.
class AuthService():

    @classmethod
    def login_user(cls, user):
        """
        The function `login_user` attempts to authenticate a user by calling a stored procedure and
        returns the authenticated user if successful.
        
        :param cls: The parameter `cls` is typically used as a reference to the class itself. It is
        commonly used in class methods to access class-level attributes or methods. However, in the
        given code snippet, the `cls` parameter is not being used, so it can be removed
        :param user: The "user" parameter is an instance of the User class. It contains the username and
        password of the user trying to log in
        :return: the authenticated user object.
        """
        try:
            connection = get_connection()
            authenticated_user = None
            with connection.cursor() as cursor:
                cursor.execute('call sp_verifyIdentity(%s, %s)', (user.username, user.password))
                row = cursor.fetchone()
                if row != None:
                    authenticated_user = User(int(row[0]), row[1], None, row[2])
            connection.close()
            return authenticated_user
        except Exception as ex:
            Logger.add_to_log("error", str(ex))
            Logger.add_to_log("error", traceback.format_exc())
