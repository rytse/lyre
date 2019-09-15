import time

import pandas as pd

from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)



# Read in all the location data
tinit = time.time()
ldata = pd.read_csv('data/locs/all.csv')

#@app.route('/')
#def mainpage():
#    return render_template('flask_test.html')

@app.route('/update/', methods=['GET'])
def hello():
    t = time.time() - tinit
    #print(t)

    dslice = ldata.loc[ldata.t < t]

    data = {}

    for dep in ['fire', 'police', 'guard']:
        data[f'{dep}_locs'] = {}
        for rep in range(5):
            data[f'{dep}_locs'][f'u{rep}'] = [dslice.tail(1)[f'{dep}_{rep}_x'].iloc[0], dslice.tail(1)[f'{dep}_{rep}_y'].iloc[0]]

    print(data)
    print('\n\n\n')

    data['alerts'] = [];
    data['disasters'] = [];
    data['dispatches'] = [];


    response = app.response_class(response=json.dumps(data),
                            status=200, mimetype='application/json');

    #response = app.response_class(response=json.dumps(f'Hello! {random.random()}'),
    #                        status=200, mimetype='application/json');

    return response;

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
