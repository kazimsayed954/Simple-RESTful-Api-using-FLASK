from flask import Flask,make_response,jsonify
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

Employee_info={
    "John":{   
        "Salary":"25L",
        'Technology':"Web Developer"
        
    },
    "kelly":{
        "Salary":"35L",
        'Technology':"ML Engineer"

    }
}

class Help(Resource):
    def get(self):
        help={
            'Available rest APIs are' :['api/v1/ping','api/v1/info','api/v1/info/ename']
        }
        return make_response(jsonify(help),200)

class ping(Resource):
    def get(self):
        status={
            'Status':'Alive'
        }
        return make_response(jsonify(status),200)
"""class Employee(Resource):
    def get(self,ename):
        return Employee_info.get(ename)"""

class Employees(Resource):
    def get(self,ename=None):
        if(ename):
            if ename in Employee_info.keys():
                return make_response(jsonify(Employee_info.get(ename)),200)
            else:
                message={
                    'Message':'Employee Not Found'
                }
                return make_response(jsonify(message),404)
        else:
            return make_response(jsonify(Employee_info),200)


api.add_resource(Employees,"/api/v1/info","/api/v1/info/<string:ename>")
#api.add_resource(Employee,"/info/<string:ename>")
api.add_resource(Help,"/")
api.add_resource(ping,'/api/v1/ping')

app.run(port=5000,host="localhost")