from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
# burgers.py
from dojos_ninjas_app import app
from flask import render_template,redirect,request,session,flash
# dojos.py...
from dojos_ninjas_app.models.dojo import Dojo
# gets all the dojos and returns them in a list of dojo objects .

@app.route('/new_dojo')
def new_dojo():
    return render_template("create_dojo.html")



@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
        "location" : request.form["location"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    Dojo.save(data)
    print(request.form)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

@app.route('/')
def dojos():
    # calling the get_all method from the dojos.py
    all_dojos=Dojo.get_all()
    # passing all dojos to our template so we can display them there
    return render_template("dojos.html",dojos=all_dojos)




@app.route('/show_dojo/<int:dojo_id>')
def show_dojo(dojo_id):
    # calling the get_one method and supplying it with the id of the dojo we want to get
    dojo=Dojo.dojos_with_ninjas(dojo_id)
    return render_template("show_dojo.html",dojo=dojo)

@app.route('/dojos/update',methods=['POST'])
def update_dojo():
    Dojo.update(request.form)
    return redirect('/')

@app.route('/dojos/delete/<int:dojo_id>')
def delete_dojo(dojo_id):
    Dojo.delete(dojo_id)
    return redirect('/')

