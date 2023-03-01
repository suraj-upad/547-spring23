# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:45:09 2023

@author: suraj
"""

import requests

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/su44")
donor = str(r.json()["Donor"])
rec = r.json()["Recipient"]
blood_donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+donor)
blood_rec = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/"+rec)
donor_type = blood_donor.text
rec_type = blood_rec.text

print(donor_type, " ", rec_type)
if donor_type == rec_type:
    ans = "Yes"
else:
    ans = "No"

out = {"Name": "su44", "Match": ans}
final = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json = out)

print(final.text)

