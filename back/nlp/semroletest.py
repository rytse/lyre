import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, SemanticRolesOptions, RelationsOptions, EntitiesOptions


MSG = 'I am at one hundred main street and we need a helicopter. There\'s a landslide at one hundred main street'
#MSG = 'A fire is destroying London'

natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
                iam_apikey='4q60I1qoSwbml9Heu_afwGa0uzw8iAo175qLdOJjX4J-',
                    url='https://gateway-syd.watsonplatform.net/natural-language-understanding/api'

        )

response = natural_language_understanding.analyze(
            text=MSG,
            features=Features(entities=EntitiesOptions())
        ).get_result()

#response = natural_language_understanding.analyze(
#                text=MSG,
#                features=Features(semantic_roles=SemanticRolesOptions())
#        ).get_result()

#print(json.dumps(response, indent=2))

####

#response = natural_language_understanding.analyze(
#                text=MSG,
#                features=Features(relations=RelationsOptions())
#            ).get_result()

print(json.dumps(response, indent=2))

