from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello"


@app.route('/index')
def main():
    return "Main"


@app.route('/user/<username>')
def user(username):
    return f'{username.upper()}\'s profile'


if __name__ == '__main__':
    app.run(debug=True)
