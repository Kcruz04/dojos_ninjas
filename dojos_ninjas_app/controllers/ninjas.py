from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
# burgers.py
from dojos_ninjas_app import app
from flask import render_template,redirect,request,session,flash
# ninjas.py...
from dojos_ninjas_app.models.ninja import Ninja
# gets all the ninjas and returns them in a list of ninja objects .
from dojos_ninjas_app.models.dojo import Dojo



@app.route('/new_ninja')
def new_ninja():
    return render_template("create_ninja.html", dojos=Dojo.get_all())


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    # print(request.form)
    # first_name = request.form[first_name]
    # last_name = request.form[last_name]
    # session[first_name] = first_name
    # session[last_name] = last_name
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "dojos_id" : request.form["dojo_id"]
    }
    print(request.form)
    # We pass the data dictionary into the save method from the Ninja class.
    Ninja.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')



@app.route('/show_dojo')
def ninjas():
    # calling the get_all method from the ninjas.py
    all_ninjas=Ninja.get_all()
    # passing all ninjas to our template so we can display them there
    return render_template("ninjas.html",ninjas=all_ninjas)

@app.route('/ninja/show/<int:ninja_id>')
def show_ninja(ninja_id):
    # calling the get_one method and supplying it with the id of the ninja we want to get
    ninja=Ninja.get_one(ninja_id)
    return render_template("show_ninja.html",ninja=ninja)

@app.route('/ninjas/update',methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    return redirect('/')

@app.route('/ninjas/delete/<int:ninja_id>')
def delete_ninja(ninja_id):
    Ninja.delete(ninja_id)
    return redirect('/')