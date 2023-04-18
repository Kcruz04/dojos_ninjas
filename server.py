from dojos_ninjas_app import app

from dojos_ninjas_app.controllers import dojos, ninjas


if __name__ == "__main__":
    app.run(debug = True, port = 5001)
    
    