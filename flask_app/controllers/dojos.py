from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route('/create', methods = ["POST"])
def create():
    data = {
        'name': request.form["name"]
    }
    Dojo.create(data)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_by_id(data), ninjas = Ninja.get_by_dojo(id))

@app.route('/ninjas')
def show_new_ninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())
