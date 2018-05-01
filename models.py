from app import db
from datetime import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


class CRUD():   

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

#creates a user table
class User(db.Model, CRUD):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(100), unique=True, index=True)
    address_1 = db.Column(db.String(200))
    address_2 = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    zip_code = db.Column(db.String(200))
    password_hash = db.Column(db.String(128))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return '<User(fullname={} {})>'.format(self.firstname, self.lastname)

#creates a student table
class Student(db.Model, CRUD):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(100), unique=True, index=True)
    address_1 = db.Column(db.String(200))
    address_2 = db.Column(db.String(200))
    city = db.Column(db.String(200))
    state = db.Column(db.String(200))
    zip_code = db.Column(db.String(200))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    student_profile = db.relationship('StudentProfile', backref="student", cascade="all, delete-orphan", uselist=False)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<Student(fullname={} {})>'.format(self.firstname, self.lastname)

#creates a student profile table
class StudentProfile(db.Model, CRUD):
    __tablename__ = 'studentprofile'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    school = db.Column(db.String(64))
    sex = db.Column(db.String(64))
    age = db.Column(db.String(64))
    address = db.Column(db.String(225))
    famsize = db.Column(db.String(64))
    pstatus = db.Column(db.String(64))
    medu = db.Column(db.String(64))
    fedu = db.Column(db.String(64))
    mjob = db.Column(db.String(64))
    fjob = db.Column(db.String(64))
    reason = db.Column(db.String(64))
    guardian = db.Column(db.String(64))
    traveltime = db.Column(db.String(64))
    studytime = db.Column(db.String(64))
    failures = db.Column(db.String(64))
    schoolsup = db.Column(db.String(64))
    famsup = db.Column(db.String(64))
    paid = db.Column(db.String(64))
    activities = db.Column(db.String(64))
    nursery = db.Column(db.String(64))
    higher = db.Column(db.String(64))
    internet = db.Column(db.String(64))
    romantic = db.Column(db.String(64))
    famrel = db.Column(db.String(64))
    freetime = db.Column(db.String(64))
    goout = db.Column(db.String(64))
    dalc = db.Column(db.String(64))
    walc = db.Column(db.String(64))
    health = db.Column(db.String(64))
    absences = db.Column(db.String(64))


    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<Student(fullname={})>'.format(self.id)
