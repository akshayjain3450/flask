#In this application you do not have to run the script again and again for every change you make
from flask import Flask
app = Flask(__name__)

@app.route('/')
def debug_hello_world():
    return "Hello, world!!!"

if __name__ == '__main__':
    app.run(debug = True)
