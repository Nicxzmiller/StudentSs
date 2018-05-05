import csv
import os
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import uuid
import pickle
import json

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def load_dataset():
    feature_name = None
    dataset = []
    label = []

#loading dataset
    with open(BASE_DIR+'/dataset/students_dataset.csv', 'r') as file:
        file_reader = csv.reader(file)
        for index, row in enumerate(file_reader):
            try:
                if index == 0:
                    feature_name = row
                    continue
                dataset.append(row[:-1])
                label.append(row[-1])
            except:
                print("error")
    return {"features":feature_name, "dataset":dataset, "labels":label}


# nominalising the dataset
def create_nominal_dataset(data_dict):
    dataset = []
    transformer = {}
    for i in range(len(data_dict['dataset'][0])):
        col = []
        skip = False
        for row in data_dict['dataset']:
            if row[i].isdigit():
                skip = True
            else:
                col.append(row[i])
        if skip:
            continue
        no_duplicate = set(col)

        for index, value in enumerate(no_duplicate):
            if i not in transformer:
                transformer[i] = {}
                transformer[i][value] = index
            else:
                transformer[i][value] = index

#transforming dataset for SVM
    for row in data_dict['dataset']:
        n_row = []
        for y, item in enumerate(row):
            if y in transformer:
                val = transformer[y][item]
                n_row.append(val)
            else:
                n_row.append(item)
        dataset.append(n_row)

    with open(BASE_DIR+"/dataset/transformer.json", 'w') as outfile:
        json.dump(transformer, outfile)

    return np.asarray(dataset, dtype=np.float32)


#training of dataset
def train_classifier(data_train, label_train):
    cost = float(input("[INPUT REQUIRED] Please input a value for the cost function (decimal):"))
    model = LinearSVC(C=cost, penalty='l2', loss="squared_hinge")
    model.fit(data_train, label_train)
    return model


#using trained dataset to test our data
def evaluate_model(model, data_test, label_test):
    model_path = BASE_DIR + "/ml_models/" + str(uuid.uuid4())+'.sav'
    predictions = model.predict(data_test)
    print(' ')
    print('===================================================================== ')
    option = input('[OPTION] SHOW PREDICTIONS [y]/n ? : ')
    if option == 'y':
        for i in range(len(predictions)):
            print('[INFO] predicted [ {} ]...expected...[ {} ]'.format(predictions[i], label_test[i]))
        print(' ')
    accuracy = accuracy_score(label_test, predictions)
    print('[INFO] ACCURACY OF PREDICTION..... ', accuracy * 100, '%')
    print(' ')
    print('===================================================================== ')
    save = input('[INFO] SAVE MODEL? ([y]/n): ')
    if save == 'y':
        pickle.dump(model, open(model_path, "wb"))
        print('[INFO] MODEL SAVED!')


def load_feature_name():
    feature_name = None
    with open(BASE_DIR+'/dataset/students_dataset.csv', 'r') as file:
        file_reader = csv.reader(file)
        for index, row in enumerate(file_reader):
            try:
                if index == 0:
                    feature_name = row
            except Exception as e:
                return None
    return feature_name
