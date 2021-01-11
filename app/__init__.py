######## IMPORTS ########

from flask import Flask
import pyrebase

######## CONFIG ###########
firebaseConfig = {
  "apiKey": "AIzaSyCaG6EmyzH2MX_3z1Dh1qQO2tzosX28yy8",
  "authDomain": "axiomatic-lamp-233710.firebaseapp.com",
  "databaseURL": "https://axiomatic-lamp-233710-default-rtdb.firebaseio.com",
  "projectId": "axiomatic-lamp-233710",
  "storageBucket": "axiomatic-lamp-233710.appspot.com",
  "messagingSenderId": "948609637485",
  "appId": "1:948609637485:web:ff833ae7ee8bca16323364",
  "measurementId": "G-624N302E6H"
}


######## INITIALIZING APP & DATABASE #########

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

app = Flask(__name__)

from app.main import *
