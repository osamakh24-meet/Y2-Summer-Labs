from flask import Flask, render_template, url_for, request, redirect
import random

app = Flask(__name__,template_folder = "templates")
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

@app.route("/home",methods=["GET", "POST"] )
def home():
    if request.method == 'POST':
        birth_month = request.form['birth_month']
        return redirect(url_for('fortune', birth_month=birth_month))
    return render_template("home.html")
   
@app.route("/fortune" )
def fortune():
    birth_month = request.args.get('birth_month', '')
    index = len(birth_month) % len(fortunes)
    chosen_fortune = fortunes[index]
    return render_template("fortune.html", fortune=chosen_fortune, birth_month=birth_month)

if __name__ == '__main__':
    app.run(debug=True)