import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, RelationsOptions

with open('transcript-0.txt', 'r') as f:
    #msg = f.readlines()[0]
    #msg = msg[0:-1]
    #print(msg)

    natural_language_understanding = NaturalLanguageUnderstandingV1(
                version='2019-07-12',
                    iam_apikey='4q60I1qoSwbml9Heu_afwGa0uzw8iAo175qLdOJjX4J-',
                    url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'

            )

    response = natural_language_understanding.analyze(
                #text='Alex Johnson won Best Developer for his performance.',
                #text='Leonardo DiCaprio won Best Actor in a Leading Role for his performance.',
                #text='Laura Jones won Best Web Developer for his performance.',
                #text='There is a fire here.',
                text='I am on fire.',
                #text=msg,
                    features=Features(relations=RelationsOptions())
            ).get_result()

    print(json.dumps(response, indent=2))
