# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:17:32 2023

@author: suraj
"""

def create_patient_entry(patient_name, patient_mrn, patient_age):
    ls = [patient_name, patient_mrn, patient_age, []]
    return ls

def main_driver():
    db=[]
    db.append(create_patient_entry('Loser Mcgee', 101, 69))
    db.append(create_patient_entry('Ben Hawk', 121, 23))
    db.append(create_patient_entry("'Mike Dover", 1032, 29))
    print(get_pat(101,db))
    update_tests(db,101,"HDL",120)
    update_tests(db,121,"HDL",100)
    update_tests(db,1032,"HDL",220)
    
    print(get_pat(101,db))
    room = ["102","34","13322"]
    print_direc(db,room)
    
    print(get_test_result(db,101,'HDL'))
    print(get_test_result(db,121,'HDL'))
    print(get_test_result(db,1032,'HDL'))


def get_pat(mrn,db):
    for p in db:
        if p[1] == mrn:
            return p
    return False
    
def update_tests(db, mrn, test_n, test_v):

    p= get_pat(mrn,db)
    if p==False:
        print("No patient")
        return
    p[3].append([test_n, test_v])
    return

def print_direc(db, room):
    for i,p in enumerate(db):
        print("patient {} is in room {}".format(p[0],room[i]))
        
def get_test_result(db, mrn, test_name):
    p = get_pat(mrn,db)
    for t in p[3]:
        if t[0]==test_name:
            return t[1]
        
    

if __name__ == "__main__":
    main_driver()