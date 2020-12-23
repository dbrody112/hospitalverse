import time
from flask import Flask,Blueprint, jsonify, request,render_template,url_for,abort
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import logging as logger
from flask_marshmallow import Marshmallow
from passlib.apps import custom_app_context as pwd_context
import sqlalchemy
from datetime import date
from datetime import datetime
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt,JWTManager)
import googlemaps
import numpy as np
import pandas as pd
from sqlalchemy.sql import func
gmaps = googlemaps.Client(<API KEY>)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://user-sha1:P@ssw0rd@localhost/hospitals"
app.config['JWT_SECRET_KEY'] = 'this-is-super-secret'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access']
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)


class Hospital(db.Model):
    __tablename__ = 'hospital'
    __table_args__ = (
            db.CheckConstraint('hospital_name IS NOT NULL'),
            db.CheckConstraint('total_score BETWEEN -1 AND 100'),
            )
    
    zip_code = db.Column(db.String(length = 6))
    #to be implemented using google maps api
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    phone_number = db.Column(db.String(length = 20))
    hospital_name = db.Column(db.String(length=100))
    website = db.Column(db.String(length = 200))
    mapsUrl = db.Column(db.String(length=200))
    total_score = db.Column(db.Integer)
    street_address = db.Column(db.String(length = 200))
    state = db.Column(db.String(length = 10))
    town = db.Column(db.String(length = 100))
    hospital_id = db.Column(db.Integer,primary_key = True)
    #* for now these columns are strings however in the future they may become integers with check constraints.
    # for the purpose of this assignment they will stay as strings
    #sub stands for sub criteria btw
    
    non_discrimination_and_staff_training = db.Column(db.String(length = 10))
    sub_patient_non_discrimination = db.Column(db.String(length = 10))
    sub_visitation_non_discrimination = db.Column(db.String(length = 10))
    sub_employment_non_discrimination = db.Column(db.String(length = 10))
    sub_staff_training = db.Column(db.String(length = 10))
    patient_services_and_support = db.Column(db.String(length = 10))
    employee_benefits_and_policies = db.Column(db.String(length = 10))
    sub_employee_policies_and_benefits = db.Column(db.String(length = 10))
    sub_transgender_inclusive_health_insurance = db.Column(db.String(length = 10))
    patient_and_community_engagement = db.Column(db.String(length = 10))
    responsible_citizenship = db.Column(db.String(length = 100))
    

class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = (
            db.CheckConstraint('username IS NOT NULL'),
            db.CheckConstraint('password IS NOT NULL'),
            )
    
    username = db.Column(db.String(length=100), primary_key = True,index=True)
    password = db.Column(db.String(300))
    sexual_orientation = db.Column(db.String(length = 100))
    age = db.Column(db.Integer)
    def hash_password(self,password):
        self.password = pwd_context.encrypt(password)
        print(len(self.password))
    def verify_password(self,password):
        return pwd_context.verify(password, self.password)
    

    
    
    
class Ratings(db.Model):

    __tablename__ = "ratings"
    username = db.Column(db.String(length=100),db.ForeignKey('users.username'),nullable = False)
    hospital_id = db.Column(db.Integer,db.ForeignKey('hospital.hospital_id'),nullable = False)
    date = db.Column(db.Date)
    rating = db.Column(db.Integer)
    verbal_rating = db.Column(db.String(length=300))
    rating_id = db.Column(db.Integer,primary_key = True)
    
    
class Hate_Groups(db.Model):
    
    __tablename__ = 'hate_groups'
    
    hospital_name = db.Column(db.String(length=100), primary_key = True)
    hate_group_name = db.Column(db.String(length = 500))
    ideology = db.Column(db.String(length = 100))
    latitude = db.Column(db.Float, primary_key = True)
    longitude = db.Column(db.Float, primary_key = True)
    distance = db.Column(db.Float)
    year = db.Column(db.Integer)

    
db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/user',methods = ['POST'])
def add_user():
    req = request.get_json()
    username = request.json.get('username')
    password = request.json.get('user_password')
    print(req)
    if username is None or password is None:
       abort(400)
    if Users.query.filter_by(username = username).first() is not None:
       abort(400)
    new_user = Users(username = username)
    new_user.hash_password(password)
    access_token = create_access_token(identity = username)
    refresh_token = create_refresh_token(identity = username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'username':new_user.username, 'access_token':access_token, 'refresh_token':refresh_token}),201, {'Location': url_for('get_user', username= new_user.username, _external = True)}

@app.route('/user/verify', methods = ['POST'])
def verify_password():
    username = request.json.get('username')
    password = request.json.get('user_password')
    user = Users.query.filter_by(username = username).first()
    if not user or not user.verify_password(password):
        return {'authorized':False}
    access_token = create_access_token(identity = username)
    refresh_token = create_refresh_token(identity = username)
    return {'authorized':True,'access_token':access_token,'username':username,'refresh_token':refresh_token}

@app.route('/users/<username>')
def get_user(username):
    user = Users.query.get(username)
    if not user:
        abort(400)
    return jsonify({'username': user.username})
    
@app.route('/user/rating', methods = ['POST'])
def add_rating():
    hospital_name = request.json.get('hospital_name')
    rating = request.json.get('rating')
    verbal_rating = request.json.get('review')
    username = request.json.get('username')
    today = date.today()
    hospital_id = db.session.query(Hospital.hospital_id).select_from(Hospital).filter(Hospital.hospital_name == hospital_name).all()[0][0]
    new_rating = Ratings(username = username,hospital_id = hospital_id, date = today, rating = rating, verbal_rating = verbal_rating)
    db.session.add(new_rating)
    db.session.commit()
    return({'hospital_id':hospital_id,'rating':rating,"success":True})
    
@app.route('/users/hospital_search', methods = ['POST'])
def hospital_search():
    street_address = request.json.get('street_address')
    town = request.json.get('town')
    state = request.json.get('state')
    zip_code = request.json.get('zip')
    radius = int(request.json.get('radius'))
    current_year = datetime.now().year
    overall_score = 0
    if(town!=None):
        town = town.title()
    
    if(state!=None):
        state = state.title()
    
    geocode_result = gmaps.geocode(str(street_address)+ " " + str(town) + " " + str(state) + " " + str(zip_code))
    latitude = np.array(geocode_result)[0]['geometry']['location']['lat']
    longitude=np.array(geocode_result)[0]['geometry']['location']['lng']
    
    hospitals = db.session.query(Hospital).all()
    phi1 = np.radians(latitude)
    
    r = 6371  # average radius of Earth in kilometers
    
   
    filtered_hospitals = []
    for hospital in hospitals:
        phi2 = np.radians(hospital.latitude)
        delta_phi = np.radians(hospital.latitude - latitude)
        delta_lambda = np.radians(hospital.longitude-longitude)
        a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
        haversine = (r*c)
        
        if(haversine*0.62137119<=radius):
            filtered_hospitals.append([hospital,haversine])
       
    score = []
    filtered_hospitals = np.array(filtered_hospitals)
    for i in filtered_hospitals[:,0]:
        score.append(i.total_score)
        #print(i.total_score)
    if(len(filtered_hospitals)==0):
        return({'success':False})
    df = pd.DataFrame({'hospitals':filtered_hospitals[:,0],'haversine':filtered_hospitals[:,1],'score':score})
    
    df = df.sort_values(by="score",ascending = False)
    df = df.sort_values(by="haversine", ascending = True)
    
    hospital_array = np.array(df['hospitals'])
    rating = 0
    ratings = [] (update but committed late)
    for i in hospital_array:
        try:
            rating = db.session.query(func.avg(Ratings.rating)).select_from(Ratings).filter(Ratings.hospital_id == i.hospital_id).all()[0][0]
        except:
            rating = 'N/A'
        #ratings.append(rating) (update but committed late (12:10 PM)
    hospital_names = []
    hospital_ids = []
    hospital_scores = []
    haversines = []
    haversine_array = np.array(df['haversine'])
    ratings = np.array(ratings) (update but committed late (12:10 PM)
    hospital = []
    #hospitals['hospital name' + str(i)] = 
    for i in range(len(hospital_array)):
        hospital.append([str(haversine_array[i]),hospital_array[i].hospital_name,str(hospital_array[i].hospital_id),str(hospital_array[i].total_score), str(ratings[i]) + "$"])
    
    return {'hospitals':hospital,'haversines':haversines,"hospital_names":hospital_names, "hospital_ids":hospital_ids, "hospital_scores": hospital_scores,'success':True}
    
@app.route('/hospital_chosen', methods = ['POST'])
    
def get_hospital_info():
    hospital_id = int(request.json.get('hospital_id'))
    print(hospital_id)
    hospital = db.session.query(Hospital).filter(Hospital.hospital_id == hospital_id).all()
    hospital = hospital[0]
    print(hospital)
    hate_groups = db.session.query(Hate_Groups).filter(Hate_Groups.hospital_name == hospital.hospital_name).all()
        
    return {"zip_code":hospital.zip_code,"phone_number":hospital.phone_number,"hospital_name":hospital.hospital_name, "website":hospital.website
    ,"mapsUrl":hospital.mapsUrl, "total_score":hospital.total_score, "street_address":hospital.street_address,"state":hospital.state,"town":hospital.town, 
    "non_discrimination_and_staff_training":hospital.non_discrimination_and_staff_training,"sub_patient_non_discrimination":hospital.sub_patient_non_discrimination,
     "sub_visitation_non_discrimination":hospital.sub_visitation_non_discrimination,"sub_employment_non_discrimination":hospital.sub_employment_non_discrimination, 
     "sub_staff_training":hospital.sub_staff_training,"patient_services_and_support":hospital.patient_services_and_support,"employee_benefits_and_policies":hospital.employee_benefits_and_policies,
     "sub_employee_policies_and_benefits":hospital.sub_employee_policies_and_benefits,"sub_transgender_inclusive_health_insurance":hospital.sub_transgender_inclusive_health_insurance,
     "patient_and_community_engagement":hospital.patient_and_community_engagement,"responsible_citizenship":hospital.responsible_citizenship, "success":True}
@app.route('/update/password', methods = ['POST'])
def update_password():
    password = request.json.get('new_password')
    oldPassword = request.json.get('old_password')
    username = request.json.get('username')
    user = Users.query.filter_by(username = username).first()
    if not user or not user.verify_password(oldPassword):
        return {'authorized':False}
    
    user.hash_password(password)
    db.session.commit()
    return {'authorized':True}

@app.route('/update/optional', methods = ['POST'])
def update_optional():
    username = request.json.get('username')
    sexual_orientation = request.json.get('sexual_orientation')
    age = request.json.get('age')
    if(len(age) == 0 and len(sexual_orientation) == 0):
        return({'empty':True})
    elif(len(age)==0):
        db.session.query(Users).filter(Users.username == username).update(dict(sexual_orientation = str(sexual_orientation)))
    elif(len(sexual_orientation)==0):
        db.session.query(Users).filter(Users.username == username).update(dict(age = int(age)))
    else:
        db.session.query(Users).filter(Users.username == username).update(dict(sexual_orientation = str(sexual_orientation), age = int(age)))
    db.session.commit()
    return({'empty':False})
