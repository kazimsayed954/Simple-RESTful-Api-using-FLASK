from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

Employee_info={
    "emp1":{
        "name":"XYZ",
        "Salary":"25L"
    },
    "emp2":{
        "name":"ABC",
        "Salary":"35L"
    }
}


class Employee(Resource):
    def get(self):
        return Employee_info
    
api.add_resource(Employee,"/info")

app.run(port=5000,host="localhost")