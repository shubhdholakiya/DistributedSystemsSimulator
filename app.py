# Imports the Flask class.
# Creates an instance of the Flask class. 
# This instance is our WSGI application.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Distributed Systems World!'

# Runs the app in debug mode, which is helpful during development as it will reload the app for you upon changes.
if __name__ == '__main__':
    app.run(debug=True)