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

class Help(Resource):
    def get(self):
        help={
            'Available rest APIs are' :['/ping','/info','/info/ename']
        }
        return help

class ping(Resource):
    def get(self):
        status={
            'Status':'Alive'
        }
        return status
"""class Employee(Resource):
    def get(self,ename):
        return Employee_info.get(ename)"""

class Employees(Resource):
    def get(self,ename=None):
        if(ename):
            return Employee_info.get(ename)
        else:
            return Employee_info


api.add_resource(Employees,"/info","/info/<string:ename>")
#api.add_resource(Employee,"/info/<string:ename>")
api.add_resource(Help,"/")
api.add_resource(ping,'/ping')

app.run(port=5000,host="localhost")