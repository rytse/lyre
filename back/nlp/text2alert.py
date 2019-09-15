import mqu

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from fuzzywuzzy import process as fprocess
import requests

emergencies_lut = ['fire', 'earthquake', 'flood', 'trapped', 'stuck', 'injured']
dispatch_lut = ['helicopter', 'helo', 'backup', 'medivac']

FEATURES = Features(keywords=KeywordsOptions())

MSG = 'I need backup at fifty first and second, there\'s a fire at the McDonalds'

def parse_sentance(msg, lat, lon):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
                version='2019-07-12',
                iam_apikey='4q60I1qoSwbml9Heu_afwGa0uzw8iAo175qLdOJjX4J-',
                url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'
            )

    response = natural_language_understanding.analyze(text=msg, features=FEATURES).get_result()
    keywords = [kw['text'] for kw in response['keywords']]

    emergency = None
    dispatch = None
    for kw in keywords:
        emergencies_rat = fprocess.extractOne(kw, emergencies_lut)
        dispatch_rat = fprocess.extractOne(kw, dispatch_lut)
        if emergencies_rat[1] > 75:
            emergency = emergencies_rat[0]
            break
        if dispatch_rat[1] > 75:
            dispatch = dispatch_rat[0]
            break

    if not (emergency or dispatch):
        return (None, None, None)

    addr = None
    for kw in keywords:
        if kw == emergency or kw == dispatch:
            continue
        addr = mqu.check_loc(kw, lat, lon)
        if addr:
            break

    return (emergency, dispatch, addr)

print('\n\n')

(e, d, a) = parse_sentance('There\'s a fire at McDonalds.', 38.9097, -77.0433)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')

(e, d, a) = parse_sentance('I need a helo sent to McDonalds.', 38.9097, -77.0433)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')

(e, d, a) = parse_sentance('I have a guy that needs medivac from Starbucks.', 39.051600, -77.174820)
print(f'Emergency: {e}\nDispatch: {d}\nAddress: {a}\n\n')
