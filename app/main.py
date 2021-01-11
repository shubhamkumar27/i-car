from flask import render_template, request
from . import app, db
from time import sleep


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/update')
def update():
    move = request.args.get('move')
    if move=='w':
        db.child("status").update({"current":"Moving Ahead"})
    elif move=='a':
        db.child("status").update({"current":"Turning Left"})
        sleep(1)
        db.child("status").update({"current":"Stopped"})
    elif move=='d':
        db.child("status").update({"current":"Turning Right"})
        sleep(1)
        db.child("status").update({"current":"Stopped"})
    elif move=='z':
        db.child("status").update({"current":"Moving Back"})
    else:
        db.child("status").update({"current":"Stopped"})
    
    return 'success'


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")