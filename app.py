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

def home():
    return render_template('home.html')

def current_weather():
    
    return



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)