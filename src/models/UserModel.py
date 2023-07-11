# The User class is a blueprint for creating user objects.
class User():
    def __init__(self, id, username, password, fullname) -> None:
        """
        The function initializes an object with the given id, username, password, and fullname.
        
        :param id: The id parameter is used to store the unique identifier for the user. It could be an
        integer or a string, depending on how you want to implement it
        :param username: The `username` parameter is used to store the username of a user. It is a
        string that represents the unique identifier for a user's account
        :param password: The `password` parameter is used to store the password for a user. It is
        typically a string that is used for authentication purposes
        :param fullname: The `fullname` parameter is a string that represents the full name of a user.
        It is used to store and retrieve the full name of a user in the class instance
        """
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname