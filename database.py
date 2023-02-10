def create_patient_entry(patient_name, patient_mrn, patient_age):
	new_patient = [patient_name, patient_mrn, patient_age, []] 
	return new_patient
	
def create_patient_entry_dict(first_name, last_name, MRN, Age):
	dict= {}
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
	#add_test_to_patient(db, 1,"LDL",120)
	#room_numbers = ["103","232","333"]
	#print(db)
	#print_directory(db, room_numbers)

def print_directory(db, room_numbers):
	for i, patient in enumerate(db):
		print("Patient {} is in room {}".format(patient[0], room_numbers[i]))

def get_patient_entry(mrn_to_find,db): 
	for patient in db:
		if patient[1] == mrn_to_find:
			return patient
	return False 

def add_test_to_patient(db, mrn, test_name, test_value):
	patient = get_patient_entry(mrn, db)
	patient[3].append([test_name, test_value])
	
if __name__ == "__main__":
	main_driver()