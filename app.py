from flask import Flask, escape, request, render_template
import random

app = Flask(__name__)

#@app.route('/')
#def mainpage():
#    return render_template('flask_test.html')

@app.route('/update/', methods=['GET'])
def hello():
    return f'Hello! {random.random()}'

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
