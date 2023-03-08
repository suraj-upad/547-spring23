# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:26:02 2023

@author: suraj
"""

import requests

patient = {"id": 1, 
           "name": "Suraj",
           "blood_type": "O+"}

test = {"id": 1,
        "test_name": "Cholesterol",
        "test_result": 100}

server = "http://127.0.0.1:5000"
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

r = requests.post(server + "/add_test", json=test)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_results/1")
print(r.status_code)
print(r.text)