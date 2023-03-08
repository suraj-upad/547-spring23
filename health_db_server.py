# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:07:40 2023

@author: suraj

{1: {"id": 1, "name": "Suraj", "blood_type": "O+", "tests": []}}
"""
import flask

from flask import Flask, jsonify, request

app = Flask(__name__)

db = {}

def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type,
                   "tests": []}
    db[id] = new_patient
    print(db)
    

def new_patient_driver(in_data):
    validation = validate(in_data)
    if validation is not True:
        return validation, 400
    add_patient_to_db(in_data['id'], in_data['name'], in_data['blood_type'])
    return "Patient added", 200

def validate(in_data):
    if type(in_data) is not dict:
        return "input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, vale_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "key {} is missing from input".format(key)
        if type(in_data[key]) is not vale_type:
            return "{} incorrect type".format(key)
    return True


def add_new_test(id, test, test_re):
    db[id]['tests'].append((test, test_re))
    print(db)
    

def new_test_driver(in_data):
    validation = validate_tests(in_data)
    if validation is not True:
        return validation, 400
    add_new_test(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Test added", 200


def id_in_db(id):
    if id in db:
        return True
    else:
        return False

def validate_tests(in_data):   
    
    if type(in_data) is not dict:
        return "input is not a dictionary"
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    for key, vale_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "key {} is missing from input".format(key)
        if type(in_data[key]) is not vale_type:
            return "{} incorrect type".format(key)
    if not id_in_db(in_data['id']):
        return "No patient with {} in db".format(in_data['id']), 400
    return True


def results_find(id):
    if not id_in_db(id):
        return "no {} here".format(id), 400
    return db[id]['tests'], 200


@app.route("/new_patient", methods = ["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer, stat_code = new_patient_driver(in_data)
    return jsonify(answer), stat_code


@app.route("/add_test", methods = ["POST"])
def post_new_test():
    in_data = request.get_json()
    answer, stat_code = new_test_driver(in_data)
    return jsonify(answer), stat_code


@app.route("/get_results/<patient_id>", methods = ["GET"])
def get_results(patient_id):
    id = int(patient_id)
    results, stat_code = results_find(id)
    return jsonify(results), stat_code
    

if __name__ == "__main__":
    app.run()
