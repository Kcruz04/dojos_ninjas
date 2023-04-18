# import the function that will return an instance of a connection
from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
# model the class after the ninja table from our database


class Ninja:
    DB = "dojos_ninjas_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # the save method will be used when we need to save a new ninja to our database


    # ... other class methods
    # class method to save our ninja to the database
    # the save method will be used when we need to save a new ninja to our database
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name,last_name, dojos_id)
        VALUES (%(first_name)s,%(last_name)s, %(dojos_id)s);"""
        return connectToMySQL(cls.DB).query_db(query,data)
    

    # @classmethod
    # def save(cls, data ):
    #     query = """INSERT INTO ninjas ( first_name, last_name, created_at, updated_at ) 
    #     VALUES ( %(first_name)s , %(last_name)s , NOW() , NOW() );"""
    #     # data is a dictionary that will be passed into the save method from server.py
    #     return connectToMySQL('dojos_ninjas_schema').query_db( query, data )
    
    # the get_all method will be used when we need to retrieve all the rows of the table 
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        if results:
            for ninja in results:
                ninjas.append( cls(ninja) )
        return ninjas
    
    # the get_one method will be used when we need to retrieve just one specific row of the table
    @classmethod
    def get_one(cls, ninja_id):
        query  = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {'id':ninja_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    # the update method will be used when we need to update a ninja in our database
    @classmethod
    def update(cls,data):
        query = """UPDATE ninjas 
                SET first_name=%(first_name)s,last_name=%(last_name)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)
    
    # the delete method will be used when we need to delete a ninja from our database
    @classmethod
    def delete(cls, ninja_id):
        query  = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id": ninja_id}
        return connectToMySQL(cls.DB).query_db(query, data)
    
    