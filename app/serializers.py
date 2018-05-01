from marshmallow import Schema, fields, post_load, ValidationError,validates
from datetime import datetime
from models import User, Student, StudentProfile
from app.validators import StringValidator

# creates user class
class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    firstname = fields.String()
    lastname = fields.String()
    address_1 = fields.String()
    address_2 = fields.String()
    city = fields.String()
    state = fields.String()
    zip_code = fields.String()
    email = fields.Email()
    last_seen = fields.DateTime(datetime.utcnow())
    password = fields.String(load_only=True)


    @post_load
    def create_user(self, data):
        user = User(firstname=data['firstname'].title(), lastname=data['lastname'].title(),
                    email=data['email'], address_1=data['address_1'],
                    address_2=data['address_2'], city=data['city'],
                    state=data['state'], zip_code=data['zip_code'])
        user.password(data['password'])
        return user

    @validates('firstname')
    def validate_firstname(self, data):
        checks = ['is_alpha']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('Firstname Should only contain Alphabets')

    @validates('lastname')
    def validate_lastname(self, data):
        checks = ['is_alpha']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('lastname Should only contain Alphabets')

    @validates('email')
    def validate_email(self, data):
        checks = ['is_email']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('Should be a valid email')


class StudentSchema(Schema):
    id = fields.Integer(dump_only=True)
    firstname = fields.String()
    lastname = fields.String()
    address_1 = fields.String()
    address_2 = fields.String()
    city = fields.String()
    state = fields.String()
    zip_code = fields.String()
    email = fields.Email()

    @post_load
    def create_student(self, data):
        student = Student(firstname=data['firstname'].title(), lastname=data['lastname'].title(),
                    email=data['email'], address_1=data['address_1'],
                    address_2=data['address_2'], city=data['city'],
                    state=data['state'], zip_code=data['zip_code'])
        return student

    @validates('firstname')
    def validate_firstname(self, data):
        checks = ['is_alpha']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('Firstname Should only contain Alphabets')

    @validates('lastname')
    def validate_lastname(self, data):
        checks = ['is_alpha']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('lastname Should only contain Alphabets')

    @validates('email')
    def validate_email(self, data):
        checks = ['is_email']
        validator = StringValidator()
        score = validator.validate(data, checks=checks)
        if not score:
            raise ValidationError('Should be a valid email')


class StudentProfile(Schema):
    id = fields.Integer(dump_only=True)
    school = fields.String()
    sex = fields.String()
    age = fields.Integer()
    address = fields.String()
    famsize = fields.String()
    pstatus = fields.String()
    medu = fields.Integer()
    fedu = fields.Integer()
    mjob = fields.String()
    fjob = fields.String()
    reason = fields.String()
    guardian = fields.String()
    traveltime = fields.Integer()
    studytime = fields.Integer()
    failures = fields.Integer()
    schoolsup = fields.String()
    famsup = fields.String()
    paid = fields.String()
    activities = fields.String()
    nursery = fields.String()
    higher = fields.String()
    internet = fields.String()
    romantic = fields.String()
    famrel = fields.Integer()
    freetime = fields.Integer()
    goout = fields.Integer()
    dalc = fields.Integer()
    walc = fields.Integer()
    health = fields.Integer()
    absences = fields.Integer()

    @post_load
    def create_student_profile(self, data):
        studentprofile = StudentProfile(school=data['school'], sex=data['sex'], age=data['age'], address=data['address'],
                                        famsize=data['famsize'], pstatus=data['pstatus'], medu=data['medu'], fedu=data['fedu'],
                                        mjob=data['mjob'], fjob=data['fjob'], reason=data['reason'], guardian=data['guardian'],
                                        traveltime=data['traveltime'], studytime=data['studytime'], failures=data['failures'],
                                        schoolsup=data['schoolsup'], famsup=data['famsup'], paid=data['paid'], activities=data['activities'],
                                        nursery=data['nursery'], higher=data['higher'], internet=data['internet'], romantic=data['romantic'],
                                        famrel=data['famrel'], freetime=data['freetime'], goout=data['goout'], dalc=data['dalc'],
                                        walc=data['walc'], health=data['health'],
                                        absences=data['absences'])
        return studentprofile