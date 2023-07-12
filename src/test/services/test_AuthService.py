from src.services.AuthService import AuthService
from src.models.UserModel import User

def test_get_authenticated_user_not_none():
    """
    The function tests that the authenticated user returned by the login_user function is not None.
    """
    _user = User(0, "ThunderGer", "abc123", None)
    authenticated_user = AuthService.login_user(_user)
    assert authenticated_user != None

def test_get_fullname_of_user_authenticated():
    """
    The function tests the functionality of retrieving the full name of an authenticated user.
    """
    _user = User(0, "ThunderGer", "abc123", None)
    authenticated_user = AuthService.login_user(_user)
    assert authenticated_user.fullname == 'Luis Gerardo Baeza'