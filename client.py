# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:39:44 2023

@author: suraj
"""

import requests

server = "http://127.0.0.1:5000"
out_data = {"a": -112, "b": 2}
r = requests.post(server + "/add", json = out_data)
print(r.status_code)
print(r.text)

r = requests.get(server+ "/add_two/1/2")
print(r.status_code)
print(r.text)