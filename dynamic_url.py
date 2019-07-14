from flask import Flask

app = Flask(__name__)

@app.route('/<string:name>')
def hello(name):
    name = name.capitalize()
    return "Hello {}!!!".format(name)

if __name__ == '__main__':
    app.run(debug = True)
