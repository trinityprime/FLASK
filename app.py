from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template("contactUs.html")

@app.route('/index')
def main():
    return "Main"


@app.route('/user/<username>')
def user(username):
    return f'{username.upper()}\'s profile'


if __name__ == '__main__':
    app.run(debug=True)
