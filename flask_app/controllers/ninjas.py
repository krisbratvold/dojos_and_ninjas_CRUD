from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo




@app.route('/ninja/create', methods = ["POST"])
def create_ninja():
    data = {
        'first_name': request.form["first_name"],
        'last_name': request.form["last_name"],
        'age': request.form["age"],
        'dojo': request.form['dojo']
    }
    Ninja.create_ninja(data)
    return redirect('/')
