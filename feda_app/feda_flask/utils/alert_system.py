import requests

def send_alert(emergency, sensor_data):
    """
    Sends an alert to the nearest hospital and police station based on the emergency and sensor data.
    
    Args:
        emergency (EmergencyDetection): The emergency detection record.
        sensor_data (SensorData): The collected sensor data.
    """
    # Code to determine the nearest hospital and police station based on the user's location
    hospital_url = 'https://example.com/api/hospital'
    police_url = 'https://example.com/api/police'
    
    # Code to send the alert to the hospital and police station
    headers = {'Content-Type': 'application/json'}
    data = {
        'emergency_type': emergency.emergency_type,
        'symptoms': emergency.symptoms,
        'heart_rate': sensor_data.heart_rate,
        'blood_pressure': sensor_data.blood_pressure,
        'temperature': sensor_data.temperature
    }
    
    requests.post(hospital_url, headers=headers, json=data)
    requests.post(police_url, headers=headers, json=data)