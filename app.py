from flask import Flask, render_template, redirect, request
from dotenv import load_dotenv

import requests
import os


app = Flask(__name__)