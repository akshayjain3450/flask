from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!!!"

@app.route('/akshay')
def hello_akshay():
    return "Hello Akshay!!!"

if __name__ == '__main__':
    app.run(debug = True)
