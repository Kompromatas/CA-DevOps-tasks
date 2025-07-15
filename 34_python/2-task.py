from flask import Flask
app = Flask(__name__)

@app.route('/hello/<username>')
def hello_to_username(username):
    return 'Hello, %s! Greetings from flask app!' %username