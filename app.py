from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

import requests
import os

from pprint import PrettyPrinter


app = Flask(__name__)

# store API key in .env 
load_dotenv()

# use pprinter
print = PrettyPrinter(indent=5)

API_KEY=os.getenv('API_KEY')
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/results')
def current_weather():
    city = request.args.get('city')
    mood = request.args.get('mood')

    params = {
        'appid': API_KEY,

        'q': city
    }

    result_json = requests.get(API_URL, params=params).json()
    print.pprint(result_json)

    context = {
        'mood': mood,
        'city': city,
        'description': result_json['weather'][0]['main']
    }
    return render_template('results.html', **context)



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)