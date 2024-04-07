from flask_login import UserMixin
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['firstaid_response_app']
users_collection = db['users']

class User(UserMixin):
    """
    Represents a user of the FirstAid Response App.
    """
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    @classmethod
    def get(cls, user_id):
        """
        Retrieves a user from the database by their ID.
        
        Args:
            user_id (str): The ID of the user to retrieve.
        
        Returns:
            User: The user object, or None if not found.
        """
        user_data = users_collection.find_one({'_id': user_id})
        if user_data:
            return cls(user_data['_id'], user_data['username'], user_data['email'])
        return None

    @classmethod
    def create(cls, username, email, password):
        """
        Creates a new user in the database.
        
        Args:
            username (str): The username of the new user.
            email (str): The email of the new user.
            password (str): The password of the new user.
        
        Returns:
            User: The new user object, or None if creation failed.
        """
        # Code to create a new user in the database
        user_id = users_collection.insert_one({'username': username, 'email': email, 'password': password}).inserted_id
        return cls(user_id, username, email)

    @classmethod
    def authenticate(cls, username, password):
        """
        Authenticates a user by their username and password.
        
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        
        Returns:
            User: The authenticated user object, or None if authentication failed.
        """
        # Code to authenticate the user by checking the username and password
        user_data = users_collection.find_one({'username': username, 'password': password})
        if user_data:
            return cls(user_data['_id'], user_data['username'], user_data['email'])
        return None