

from logger import logger

from flask import render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from app import app, login_manager
from analyzer import load_data, get_student_view, get_mentor_view

# Dummy user store
users = {
    'alice': {'password': '123', 'role': 'student'},
    'preeti': {'password': '456', 'role': 'mentor'}
}

class User(UserMixin):
    def __init__(self, username, role):
        self.id = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    role = users[user_id]['role']
    return User(user_id, role)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User(username, users[username]['role'])
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    data = load_data()
    if current_user.role == 'student':
        student_view = get_student_view(current_user.id, data)
        return render_template('student_dashboard.html', student=student_view)
    else:
        sort_by = request.args.get('sort', 'Grade')
        filter_result = request.args.get('result')
        mentor_view = get_mentor_view(data, sort_by, filter_result)
        return render_template('mentor_dashboard.html', students=mentor_view)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/export')
@login_required
def export():
    if current_user.role != 'mentor':
        return "Unauthorized", 403

    data = load_data()
    summary = get_mentor_view(data)
    summary.to_excel('data/exported_summary.xlsx', index=False)
    logger.info(f"Mentor {current_user.id} exported student summary.")
    return "Exported successfully!"

from logger import logger

logger.info("User alice logged in successfully.")
logger.warning("Missing grades found and filled with 0.")
logger.error("Failed to load students.csv")

