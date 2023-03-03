# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:17:07 2023

@author: suraj
"""

import flask

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/HDL_analysis", methods = ["POST"])
def HDL_route_handler():
    """
    in_data = {"name": <patient_name>,
               "HDL_value": <HDL_result>}

    """
    from blood_calculator import hdl_anal
    in_data = request.get_json()
    diagnosis = hdl_anal(in_data["HDL_value"])
    return diagnosis 
    
@app.route("/add", methods = ["POST"])
def add_stuff():
    in_data = request.get_json()
    a = in_data["a"]
    b = in_data["b"]
    if a+b < 0 :
        return "The answer negative, bad bro do better", 400
    return jsonify(a+b)

@app.route("/add_two/<a>/<b>", methods = ["GET"])
def add_two(a,b):
    return jsonify(int(a)+int(b))

if __name__ == "__main__":
    app.run()