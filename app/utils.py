import json
import time
import random
import os
import dotenv
import requests

dotenv.load_dotenv('.env')

def simulate_vehicle(origin,destination,time_multiplier):
    google_cloud_key=os.environ.get('GOOGLE_CLOUD_KEY')
    url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&key={}".format(origin,destination,google_cloud_key)
    response = requests.request("GET",url)
    
    data = json.loads(response.text)
    
    
    time_multiplier = 10
    steps = data['routes'][0]['legs'][0]['steps']
    for step in steps:
        location = step['end_location']
        lat = location['lat']
        lng = location['lng']
        duration = step['duration']['text'].split(' ')[0]
        print(f"""
            Vehicle in ( {lat} , {lng} ).
            Next point in {duration} min.
            Current vehicle speed is {random.randint(50,80)}.{random.randint(0,99)}      
            """)
        time.sleep(float(duration)/time_multiplier*6)