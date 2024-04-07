from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['firstaid_response_app']
sensor_data_collection = db['sensor_data']

class SensorData:
    """
    Represents sensor data collected during an emergency detection.
    """
    def __init__(self, id, user_id, emergency_id, heart_rate, blood_pressure, temperature):
        self.id = id
        self.user_id = user_id
        self.emergency_id = emergency_id
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.temperature = temperature

    @classmethod
    def collect(cls, user_id, emergency):
        """
        Collects sensor data during an emergency detection.
        
        Args:
            user_id (str): The ID of the user who detected the emergency.
            emergency (EmergencyDetection): The emergency detection record.
        
        Returns:
            SensorData: The collected sensor data.
        """
        # Code to collect sensor data (heart rate, blood pressure, temperature)
        sensor_data_id = sensor_data_collection.insert_one({'user_id': user_id, 'emergency_id': emergency.id, 'heart_rate': 80, 'blood_pressure': '120/80', 'temperature': 98.6}).inserted_id
        return cls(sensor_data_id, user_id, emergency.id, 80, '120/80', 98.6)