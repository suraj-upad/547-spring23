def create_patient_entry(first_name, last_name, patient_mrn, patient_age):
    new_patient = {"First Name":first_name,
                   "Last Name": last_name,
                   "MRN": patient_mrn,
                   "Age": patient_age,
                   "Tests":[]}
    return new_patient


def main_driver():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 34))
    db.append(create_patient_entry("Bob","Boyles", 2, 45))
    db.append(create_patient_entry("Chris","Chou", 3, 52))
    #print(db)
    print_database(db)
    add_test_to_patient(db, 1, "HDL", 120)
    add_test_to_patient(db, 2, "LDL", 100)
    add_test_to_patient(db, 2, "HDL", 99)
    room_numbers = ["103", "232", "333"]
    print(db)
    print("Chris Chou is an {}".format(minor_or_adult(db[2])))
    return
    print_directory(db, room_numbers)
    print(get_test_result(db, 2, "LDL"))


def get_full_name(patient):
    first = patient["First Name"]
    last = patient["Last Name"]
    name = first + " " + last
    return name


def print_database(db):
    for patient in db:
        mrn = patient["MRN"]
        name = get_full_name(patient)
        age = patient["Age"]
        print("MRN: {}, Full Name: {}, Age: {}".format(mrn, name, age))


def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))
    for patient, rn in zip(db, room_numbers):
        print("Patient {} is in room {}".format(patient[0], rn))


def get_patient_entry(db, mrn_to_find):
    for patient in db:
        if patient["MRN"] == mrn_to_find:
            return patient
    return False


def add_test_to_patient(db, mrn_to_find, test_name, test_value):
    patient = get_patient_entry(db, mrn_to_find)
    if patient is False:
        print("Bad entry")
    else:
        patient["Tests"].append([test_name, test_value])
    return


def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False


def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_value_from_test_list(patient["Tests"], test_name)
    return test_value

def minor_or_adult(patient):
    if patient["Age"]<18:
        return "minor"
    else:
        return "adult"

if __name__ == "__main__":
    main_driver()