def create_patient_entry(patient_name, patient_mrn, patient_age):
	new_patient = [patient_name, patient_mrn, patient_age] 
	return new_patient

def main_driver():
	db = []
	db.append(create_patient_entry("Ann", 1, 34))
	db.append(create_patient_entry("Save", 2, 45))
	db.append(create_patient_entry("dave", 3, 50))
	print(db)
	print("Get patient Ann")
	found_patient = get_patient_entry(4,db)
	if found_patient is False: 
		print("Patient mrn not found")
	else:
		print(found_patient)

def get_patient_entry(mrn_to_find,db): 
	for patient in db:
		if patient[1] == mrn_to_find:
			return patient
	return False 
	
if __name__ == "__main__":
	main_driver()