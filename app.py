import time

import pandas as pd

from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS
import random

# Flask setup
app = Flask(__name__)
CORS(app)   # allow React to read this while running in 1234, not 5000

# Read in all the location data
tinit = time.time()
ldata = pd.read_csv('data/locs/all.csv')

@app.route('/update/', methods=['GET'])
def hello():
    t = time.time() - tinit
    dslice = ldata.loc[ldata.t < t]
    data = {}

    # Add location data (latest known location, regardless of last update)
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

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
