from flask import session as login_session
from flask import Flask, render_template, request, redirect, url_for, flash
import pyrebase 

app = Flask(__name__, template_folder='templates', static_folder='static') 
app.config['SECRET_KEY'] = 'super-secret-key'

firebaseConfig = {
    'apiKey': "AIzaSyCA9prNf22vvbIRkv8_4JP12lsnKWWkN-U",
    'authDomain': "labb-e7efa.firebaseapp.com",
    'projectId': "labb-e7efa",
    'storageBucket': "labb-e7efa.appspot.com",
    'messagingSenderId': "191422834722",
    'appId': "1:191422834722:web:cacc70dbbf07e9c9ab427b",
    'measurementId': "G-QWELJT8KF9",
    "databaseURL": "https://indevedual-project-default-rtdb.europe-west1.firebasedatabase.app/"
} 

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() 
db = firebase.database() 

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except:
            flash('Email already exists or password is too weak.', 'danger')
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            login_session['user'] = user['localId']
            return redirect(url_for('home'))
        except:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    login_session.pop('user', None)
    return redirect(url_for('welcome'))

@app.route('/home')
def home():
    if 'user' not in login_session:
        return redirect(url_for('login'))
    return render_template('home.html', user=login_session['user'])

@app.route('/gossip', methods=['GET', 'POST'])
def gossip():
    if 'user' not in login_session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        gossip_text = request.form['gossip']
        db.child("gossips").push({"text": gossip_text, "user": login_session['user']})
        return redirect(url_for('gossipsum'))
    return render_template('gossip.html')

@app.route('/gossipsum')
def gossipsum():
    if 'user' not in login_session:
        return redirect(url_for('login'))
    gossips = db.child("gossips").get().val()
    return render_template('gossipsum.html', gossips=gossips)

if __name__ == '__main__':
    app.run(debug=True)


