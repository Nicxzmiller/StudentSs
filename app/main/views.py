from flask import render_template, request, redirect,url_for, session
from . import main
from app.serializers import UserSchema, StudentSchema
from models import User, Student, StudentProfile
import copy
from app import db


@main.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@main.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    if request.method == "POST":
        try:
            schema = UserSchema(strict=True)
            data = request.form
            result = schema.load(data)
            user = result.data
            if User.query.filter_by(email=user.email).first():
                return redirect(url_for("main.login"))
            else:
                user.add()
                session['user'] = user.email
                return redirect(url_for('main.dashboard'))
        except:
            return "error"
    return "method not allowed"


@main.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        data = dict(request.form.to_dict(flat=True))
        print(data)
        if not bool(data):
            return redirect(url_for("main.login"))
        user = User.query.filter_by(email=data['email']).first()
        if user and user.verify_password(data['password']):
            session['user'] = user.email
            return redirect(url_for("main.dashboard"))
        else:
            return redirect(url_for("main.login"))
    return "method not allowed"


@main.route('/dashboard', methods=["GET"])
def dashboard():
    try:
        user_email = session['user']
    except:
        user_email = None
    if user_email:
        return render_template('dashboard.html')
    else:
        return redirect(url_for("main.login"))


@main.route('/registerstudent', methods=["GET", "POST"])
def registerstudent():
    if request.method == "GET":
        return render_template('registerstudent.html')
    if request.method == "POST":
        try:
            schema = StudentSchema(strict=True)
            data = request.form.to_dict(flat=True)
            result = schema.load(data)
            student = result.data
            if Student.query.filter_by(email=student.email).first():
                return redirect(url_for("main.registerstudent"))
            else:
                student.add()
                return redirect(url_for('main.dashboard'))
        except:
            return "error"
    return "method not allowed"


@main.route('/studentprofile', methods=["GET", "POST"])
def profile():
    if request.method == "GET":
        return render_template('studentprofile.html', student=Student.query.filter_by(id=request.args.get('student')).first())
    if request.method == "POST":
        student_id = request.args.get('student')
        student = Student.query.filter_by(id=student_id).first()
        data = request.form.to_dict(flat=True)
        data.pop("submit")
        try:
            profile = StudentProfile(**data)
            student.student_profile = profile
            profile.add()
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            print(e)
            return "error"
    return "method not allowed"


@main.route("/students", methods=["GET"])
def get_students():
    try:
        user_email = session['user']
    except:
        user_email = None
    if user_email:
        students = Student.query.order_by(Student.firstname).all()
        return render_template("viewstudents.html", students=students)
    else:
        return redirect(url_for("main.login"))


@main.route("/student/info", methods=["GET"])
def get_student():
    try:
        user_email = session['user']
    except:
        user_email = None
    if user_email:
        student_id = request.args.get('student')
        student = Student.query.filter_by(id=student_id).first()
        data = copy.deepcopy(student.__dict__)
        data.pop('_sa_instance_state')

        profile = student.student_profile
        if profile is None:
            return render_template("404.html")
        profile_dict = copy.deepcopy(profile.__dict__)
        profile_dict.pop('_sa_instance_state')
        profile_dict.pop("student_id")

        return render_template("student.html", student=data, profile=profile_dict)
    else:
        return redirect(url_for("main.login"))