from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    name = session.get('name')
    if name is None:
        return redirect(url_for('login'))
    return render_template('home.html', name=name)

@app.route('/fortune', methods=['GET'])
def fortune():
    birth_month = session.get('birth_month')
    if birth_month is None:
        return redirect(url_for('login'))
    fortunes = [
        "You will have a great day!",
        "Something unexpected will happen.",
        "You will achieve your goals.",
        "Happiness is coming your way.",
        "Be cautious of new opportunities.",
        "A pleasant surprise is in store for you.",
        "You will meet someone special soon.",
        "A new adventure is on the horizon.",
        "Today is your lucky day!",
        "Expect good news in the coming days."
    ]
    index = len(birth_month) % len(fortunes)
    chosen_fortune = fortunes[index]
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)