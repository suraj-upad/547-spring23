# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:17:32 2023

@author: suraj
"""

def create_patient_entry(patient_name, patient_mrn, patient_age):
    ls = [patient_name, patient_mrn, patient_age]
    return ls

def main_driver():
    db=[]
    db.append(create_patient_entry('Loser Mcgee', 101, 69))
    db.append(create_patient_entry('Ben Hawk', 121, 23))
    db.append(create_patient_entry("'Mike Dover", 1032, 29))
    print(get_pat(101,db))

def get_pat(mrn,db):
    for p in db:
        if p[1] == mrn:
            return p
    return False
    

if __name__ == "__main__":
    main_driver()