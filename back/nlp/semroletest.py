import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from fuzzywuzzy import process as fprocess
import requests

emergencies_lut = ['fire', 'earthquake', 'flood', 'trapped', 'stuck', 'injured']
dispatch_lut = ['helicopter', 'helo', 'backup', 'medivac']

#MSG = 'I am at one hundred main street and we need a helicopter. There\'s a landslide at one hundred main street'
#MSG = 'There\'s a landslide at one hundred main street'
#MSG = 'There\'s a fire at one hundred main street'
#MSG = 'A fire is destroying London'

FEATURES = Features(keywords=KeywordsOptions())

MSG = 'I need backup at fifty first and second, there\'s a fire at the McDonalds'

def search_loc(kw):


def parse_sentance(msg):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
                version='2019-07-12',
                iam_apikey='4q60I1qoSwbml9Heu_afwGa0uzw8iAo175qLdOJjX4J-',
                url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'
            )

    response = natural_language_understanding.analyze(text=msg, features=FEATURES).get_result()
    keywords = [kw['text'] for kw in response['keywords']]

    for kw in keywords:
        emergencies_rat = fprocess.extractOne(kw, emergencies_lut)
        dispatch_rat = fprocess.extractOne(kw, dispatch_rat)
