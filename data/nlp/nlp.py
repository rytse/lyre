import requests
import json

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

from fuzzywuzzy import process as fprocess


# Location parsing constants
place_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
dist_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'


def check_loc(msg, lat, lon):
    '''
    Check if a string refers to a building that Google Maps API can find
    near the location specified by (lat, lon).
    '''
    place_params = {'input': msg,
             'inputtype': 'textquery',
             'fields':'name,formatted_address',
             'locationbias': f'circle:5@{lat},{lon}',
             'key': 'AIzaSyAD0_7dEG0LlC0JNuHn5QHIeW3CNOFdbmY'}

    r = requests.get(url=place_url, params=place_params)
    data = r.json()

    if len(data['candidates']) > 0:
        addr = data['candidates'][0]['formatted_address']
        dist_params = {'origins': f'{lat},{lon}',
                       'destinations': addr,
                       'fields': 'duration',
                       'key': 'AIzaSyAD0_7dEG0LlC0JNuHn5QHIeW3CNOFdbmY'}
        r = requests.get(url=dist_url, params=dist_params)
        data = r.json()
        dist = data['rows'][0]['elements'][0]['distance']['value'] / 1e3    # distance in km

        if dist < 5:
            return addr
        else:
            return None

    else:
        return None


# Text parsing constants
EMERGENCIES_LUT = ['fire', 'earthquake', 'flood', 'trapped', 'stuck', 'injured']
DISPATCH_LUT = ['helicopter', 'helo', 'backup', 'medivac']
FEATURES = Features(keywords=KeywordsOptions())


def parse_sentance(msg, lat, lon):
    '''
    Parse an input sentance using a combination of IBM Watson's smart keyword searching,
    vanilla pattern recognition for emergencies and dispatches, and the Google Maps API
    for locations.
    '''
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
        emergencies_rat = fprocess.extractOne(kw, EMERGENCIES_LUT)
        dispatch_rat = fprocess.extractOne(kw, DISPATCH_LUT)
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
        addr = check_loc(kw, lat, lon)
        if addr:
            break

    return (emergency, dispatch, addr)
