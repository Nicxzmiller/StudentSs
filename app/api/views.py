import pickle
import json
import copy
import numpy as np
from flask import render_template, request, redirect,url_for
from . import api
from models import User, Student, StudentProfile
from app import BASE_DIR
from src.utils import load_feature_name

classifier = pickle.load(open(BASE_DIR + "/src/ml_models/3c812296-fcbf-45e1-bb15-a1a148977e72.sav", 'rb'))
feature_names = load_feature_name()

with open(BASE_DIR + '/src/dataset/transformer.json', 'r') as file:
    data = ""
    for row in file:
        data += row
    transformer = json.loads(data)


@api.route('/report', methods=["GET", "POST"])
def report():
    student_id = request.args.get('id')
    student = Student.query.filter_by(id=student_id).first()

    student_dict = copy.deepcopy(student.__dict__)
    student_dict.pop('_sa_instance_state')

    student_profile = student.student_profile
    data = copy.deepcopy(student_profile.__dict__)
    data.pop('_sa_instance_state')

    serialized = []
    nominal = []
    for feature in feature_names[:-1]:
        serialized.append(data[feature.lower()])

    for index, val in enumerate(serialized):
        try:
            mapping = transformer[str(index)]
            nominal.append(mapping[val])
        except KeyError:
            nominal.append(val)

    result = classifier.predict(np.asarray([nominal], dtype=np.float32))

    return render_template("statistics.html", result=result, student=student_dict)

