from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['firstaid_response_app']
emergencies_collection = db['emergencies']

class EmergencyDetection:
    """
    Represents an emergency detection record in the FirstAid Response App.
    """
    def __init__(self, id, user_id, emergency_type, image, symptoms):
        self.id = id
        self.user_id = user_id
        self.emergency_type = emergency_type
        self.image = image
        self.symptoms = symptoms

    @classmethod
    def create(cls, user_id, emergency_type, image, symptoms):
        """
        Creates a new emergency detection record in the database.
        
        Args:
            user_id (str): The ID of the user who detected the emergency.
            emergency_type (str): The type of emergency detected.
            image (bytes): The image of the emergency.
            symptoms (str): The symptoms entered by the user.
        
        Returns:
            EmergencyDetection: The new emergency detection record.
        """
        emergency_id = emergencies_collection.insert_one({'user_id': user_id, 'emergency_type': emergency_type, 'image': image, 'symptoms': symptoms}).inserted_id
        return cls(emergency_id, user_id, emergency_type, image, symptoms)