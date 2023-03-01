# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:21:14 2023

@author: suraj
"""

import requests

# out= {"name": "Suraj Upadhya",
#       "net_id": "su44",
#       "e-mail": "su44@duke.edu"}

# r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out)


message = {"user": "xw172",
           "message": "Time for you to think about life really deeply ;)"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=message)


r2 = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/su44")
print(r2.status_code)
print(r2.text)