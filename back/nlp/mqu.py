import requests
import json

place_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
dist_url = 'https://maps.googleapis.com/maps/api/distancematrix/json'

def check_loc(msg, lat, lon):
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
