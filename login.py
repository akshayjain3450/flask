#Do not name the file with any such word which can give you namespace error
#run both the files login.html and login.py
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<string:name>')
def success(name):
    return "Welcome {}".format(name)

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug = True)
