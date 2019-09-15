from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

#@app.route('/')
#def mainpage():
#    return render_template('flask_test.html')

@app.route('/update/', methods=['GET'])
def hello():
    response = app.response_class(response=json.dumps(f'Hello! {random.random()}'),
                            status=200, mimetype='application/json');
    return response;
    #return jsonify(f'Hello! {random.random()}')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
