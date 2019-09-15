import time

import pandas as pd

from flask import Flask, escape, request, render_template, json, jsonify
from flask_cors import CORS
import random

# Flask setup
app = Flask(__name__)
CORS(app)   # allow React to read this while running in 1234, not 5000

# Read in all the location data
tprev = time.time()
tinit = time.time()
ldata = pd.read_csv('data/locs/all.csv')
adata = pd.read_csv('data/nlp/all.csv')

def clean_list(L):
    return [rep for rep in L if str(rep) != 'nan']

@app.route('/update/', methods=['GET'])
def hello():
    #try:
    #    adata = adata.loc[adata['Time'] >= t]
    #except:
    #    pass

    t = time.time() - tinit
    l_dslice = ldata.loc[ldata.t < t]

    a_dslice = adata.loc[adata['Time'] < t]

    tprev = time.time()

    data = {}

    # Add location data (latest known location, regardless of last update)
    for dep in ['fire', 'police', 'guard']:
        data[f'{dep}_locs'] = {}
        for rep in range(5):
            data[f'{dep}_locs'][f'u{rep}'] = [l_dslice.tail(1)[f'{dep}_{rep}_x'].iloc[0], l_dslice.tail(1)[f'{dep}_{rep}_y'].iloc[0]]

    # Add alert data
    data['alerts'] = clean_list(list(a_dslice['Alert']))
    data['disasters'] = clean_list(list(a_dslice['Emergency']))
    data['dispatches'] = clean_list(list(a_dslice['Dispatch']))

    print(data)
    print('\n\n\n')

    response = app.response_class(response=json.dumps(data),
                            status=200, mimetype='application/json');

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
