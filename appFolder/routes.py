from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from appFolder.models import User, Plant, UserPlant
from werkzeug.security import generate_password_hash, check_password_hash
from appFolder import app, db, api

resource_fields = {
    'user_id': fields.Integer,
    'email': fields.String,
    'username': fields.String,
    'phoneNumber': fields.String,
    'password': fields.String,
}
plant_fields = {
    'plant_id': fields.Integer,
    'name': fields.String,
    'location': fields.String,
    'use': fields.String,
    'imagePath': fields.String,
    'user_id': fields.String,
    'approved': fields.String,
    'price': fields.Float,
}

#signin or login

class UseSignIn(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password'] 
        result = User.query.filter_by(email=email).first()
        if result:
            if result.password == password:
                return {"message":"login"}
        return {"message":"not login"} 

#signup or register

class UserSignUp(Resource):
    @marshal_with(resource_fields)
    def post(self):
        new_user = User()
        new_user.email = request.json['email']
        new_user.username = request.json['username']
        new_user.phoneNumber = request.json['phoneNumber']
        new_user.password = request.json['password']

        db.session.add(new_user)
        db.session.commit()
        return new_user

class Plants(Resource):
    @marshal_with(plant_fields)
    def post(self,user_id):
        new_user = Plant()
        new_user.name = request.json['name']
        new_user.location = request.json['location']
        new_user.use = request.json['use']
        new_user.imagePath = request.json['imagePath']
        new_user.user_id = user_id

        db.session.add(new_user)
        db.session.commit()
        result=Plant.query.filter_by(name=request.json['name']).first()
        userPlant = UserPlant()
        userPlant.user_id = user_id
        userPlant.plant_id = result.plant_id
        db.session.add(userPlant)
        db.session.commit()
        return new_user

class AllPlant(Resource):
    @marshal_with(plant_fields)
    def get(self):
        result = Plant.query.all()
        if result:
            return result
        return {"noting":"found"}

class OnePlant(Resource):
    @marshal_with(plant_fields)
    def get(self, id):
        result=Plant.query.filter_by(plant_id=id).all()
        if result:
            return result
        return "recipe id not found"

class BuyPlant(Resource):
    @marshal_with(plant_fields)
    def get(self, user_id):
        res=[]
        result=UserPlant.query.filter_by(user_id=user_id).all()
        for i in result:
           res.append(i.plant_id)
        print(res)
        print()
        
        for i in range (len(res)):
           final = res[i]
           finalRes = Plant.query.filter_by(plant_id=final).all()
           if finalRes:
               return finalRes
        return "not found"

class GetPosted(Resource):
    @marshal_with(plant_fields)
    def get(self, user_id):
        result=Plant.query.filter_by(user_id=user_id).all()
        if result:
            return result
        return "recipe id not found"

#search

class UserSearch(Resource):
    @marshal_with(plant_fields)
    def get(self, search_term):
        results = Plant.query.filter(Plant.name.like('%'+search_term+'%')).all()
        if results:
            return results
        return {"result": "not found"}




api.add_resource(UseSignIn, "/api/v1/user/login")
api.add_resource(UserSignUp,  "/api/v1/user/register")
api.add_resource(Plants, '/api/v1/user/plant/<user_id>')
api.add_resource(AllPlant, '/api/v1/user/plants')
api.add_resource(OnePlant, '/api/v1/user/oneplants/<id>')
api.add_resource(BuyPlant, '/api/v1/user/buyplants/<user_id>')
api.add_resource(GetPosted, '/api/v1/user/getplants/<user_id>')
api.add_resource(UserSearch, '/api/v1/user/searchplants/<search_term>')











