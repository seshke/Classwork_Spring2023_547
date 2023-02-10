def create_patient_entry(patient_name, patient_mrn, patient_age):
    new_patient = [patient_name, patient_mrn, patient_age, []]
    return new_patient


def create_patient_entry_dict(first_name, last_name, MRN, Age):
    dict = {}
    dict['First Name'] = first_name
    dict['Last Name'] = last_name
    dict['MRN'] = MRN
    dict['Age'] = Age
    dict['Tests'] = []
    return dict


def main_driver():
    db = []
    db.append(create_patient_entry_dict("Ann",'Abbles', 1, 34))
    db.append(create_patient_entry_dict("Save",'Help', 2, 45))
    db.append(create_patient_entry_dict("dave",'davis', 3, 50))
    print(db)
    print_database(db)
    add_test_to_patient(db, 1,"LDL",120)
    #room_numbers = ["103","232","333"]
    #print(db)
    #print_directory(db, room_numbers)
 
    
def get_full_name(patient_dict):
    return patient_dict['First Name']+ ' ' + patient_dict['Last Name'] 
   
 
def print_database(db):
    for entry in db:
        result = str(entry['MRN']) +", Full Name: " + get_full_name(entry)+ ", Age: " + str(entry['Age']) 
        print(result)
  
        
def print_directory(db, room_numbers):
    for i, patient in enumerate(db):
        print("Patient {} is in room {}".format(patient[0], room_numbers[i]))


def get_patient_entry(mrn_to_find,db): 
    for patient in db:
        if patient['MRN'] == mrn_to_find:
            return patient
    return False 


def add_test_to_patient(db, mrn, test_name, test_value):
    patient = get_patient_entry(mrn, db)
    patient['Tests'].append([test_name, test_value])


def get_test_value_from_test_list(test_list, test_name):
    for test in test_list:
        if test[0] == test_name:
            return test[1]
    return False


def get_test_result(db, mrn, test_name):
    patient = get_patient_entry(db, mrn)
    test_value = get_test_value_from_test_list(patient['Tests'], test_name)
    return test_value
    

if __name__ == "__main__":
    main_driver()
    
    