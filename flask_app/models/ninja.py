from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = ['first_name']
        self.last_name = ['last_name']
        self.age = ['age']
        self.created_at = ['created_at']
        self.updated_at = ['updated_at']
        self.dojo_id = ['dojo_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def get_by_dojo(cls,id):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        data ={
            "id":id
        }
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name,last_name,age,dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo)s);"
        ninja_id = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return ninja_id