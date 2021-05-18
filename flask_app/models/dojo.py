from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return dojo_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(results[0])
