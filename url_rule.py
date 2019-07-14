
#we can define different functions and put all the routes together for each function. no immediate child required
from flask import Flask
app = Flask(__name__)

def hello_world():
    return "Hello World!!!"


def total():
    num1, num2 = 5 ,6
    total = num1 + num2
    return "11"

app.add_url_rule('/hello','hello',hello_world)
app.add_url_rule('/total','total',total)

if __name__ == '__main__':
    app.run(debug = True)
