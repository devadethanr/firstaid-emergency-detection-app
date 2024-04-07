from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.user import User
from models.emergency_detection import EmergencyDetection
from models.sensor_data import SensorData
from utils.cnn_model import detect_emergency
from utils.alert_system import send_alert

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """
    Loads the user object from the database.
    
    Args:
        user_id (str): The ID of the user to be loaded.
    
    Returns:
        User: The user object.
    """
    return User.get(user_id)

@app.route('/')
def index():
    """
    Renders the home page.
    """
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles the login process.
    """
    if request.method == 'POST':
        user = User.authenticate(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    """
    Logs out the current user.
    """
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles the user registration process.
    """
    if request.method == 'POST':
        user = User.create(request.form['username'], request.form['email'], request.form['password'])
        if user:
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Please try again.', 'danger')
    return render_template('register.html')

@app.route('/emergency-detection', methods=['GET', 'POST'])
@login_required
def emergency_detection():
    """
    Handles the emergency detection process.
    """
    if request.method == 'POST':
        image = request.files['image']
        symptoms = request.form['symptoms']
        emergency_type = detect_emergency(image, symptoms)
        if emergency_type:
            emergency = EmergencyDetection.create(current_user.id, emergency_type, image, symptoms)
            sensor_data = SensorData.collect(current_user.id, emergency)
            send_alert(emergency, sensor_data)
            return render_template('video_player.html', video_url=get_video_url(emergency_type))
        else:
            flash('No emergency detected. Please try again.', 'danger')
    return render_template('emergency_detection.html')

def get_video_url(emergency_type):
    """
    Retrieves the URL of the video solution for the given emergency type.
    
    Args:
        emergency_type (str): The type of emergency.
    
    Returns:
        str: The URL of the video solution.
    """
    # Code to retrieve the video URL based on the emergency type
    return 'https://example.com/video/solution.mp4'

if __name__ == '__main__':
    app.run()