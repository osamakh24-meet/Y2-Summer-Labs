from flask import Flask, render_template
import random

app = Flask(__name__,template_folder = "templates")

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/fortune')
def fortune():
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
    chosen_fortune = random.choice(fortunes)
    return render_template('fortune.html', fortune=chosen_fortune)

if __name__ == '__main__':
    app.run(debug=True)