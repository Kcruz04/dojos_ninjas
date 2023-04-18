# import the function that will return an instance of a connection
from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from dojos_ninjas_app.models import ninja

# model the class after the dojo table from our database
class Dojo:
    DB = "dojos_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def dojos_with_ninjas( cls , id):
        data = {"id":id}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo

    # the get_all method will be used when we need to retrieve all the rows of the table 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    # @classmethod
    # def get_all(cls):
    #     query = "SELECT * FROM dojos;"
    #     # make sure to call the connectToMySQL function with the schema you are targeting.
    #     results = connectToMySQL('dojos_ninjas_schema').query_db(query)
    #     # Create an empty list to append our instances of friends
    #     dojos = []
    #     # Iterate over the db results and create instances of friends with cls.
    #     for dojo in results:
    #         dojos.append( cls(dojo) )
    #     return dojos

    # the save method will be used when we need to save a new dojo to our database
    
    @classmethod
    def save(cls, data):
            query = """INSERT INTO dojos (name, location)
            VALUES (%(name)s,%(location)s);"""
            result = connectToMySQL(cls.DB).query_db(query,data)
            return result


    # ... other class methods
    # class method to save our dojo to the database
    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO dojos ( name , location , created_at, updated_at ) VALUES ( %(name)s , %(location)s , NOW() , NOW() );"
    #     # data is a dictionary that will be passed into the save method from server.py
    #     return connectToMySQL('dojos_ninjas_schema').query_db( query, data )
    

    
    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, dojo_id):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {'id':dojo_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    # the update method will be used when we need to update a dojo in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE dojos 
                SET name=%(name)s,location=%(location)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    # the delete method will be used when we need to delete a dojo from our database
    @classmethod
    def delete(cls, dojo_id):
        query  = "DELETE FROM dojos WHERE id = %(id)s;"
        data = {"id": dojo_id}
        return connectToMySQL(cls.DB).query_db(query, data)

