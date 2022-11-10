from flask import Flask, request
from flask_restful import Resource, Api

print(__name__)
app = Flask (__name__) ## instance of this API through Flask class, __name__ becomes main
api = Api(app) ## put instance of Flask class into API class 

class HelloWorld(Resource): #class Helloworld inherits from class Resource
    def get(self): #self - variable that contains all params of the class
        return {'hello':'world'} #dictionary returns to follow JSON format <key>:<value>


api.add_resource(HelloWorld, '/') # instance of the Api class calls upon a method add_resource

todos={} #creating a dictionary

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id:todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/todos/<string:todo_id>')

class Todos(Resource):
    def get(self):
        return todos

api.add_resource(Todos,'/todos')

if __name__ == '__main__': #when you import the app,__name__ = name of the app e.g. "api" in this case;
    
    app.run(debug=True) #each time you run the app, the __name__ automatically turns into __main__