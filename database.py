def create_patient_entry(patient_name, patient_mrn, patient_age):
	new_patient = [patient_name, patient_mrn, patient_age] 
	return new_patient

def main_driver():
	db = []
	db.append(create_patient_entry("Ann", 1, 34))
	db.append(create_patient_entry("Save", 2, 45))
	db.append(create_patient_entry("dave", 3, 50))
	print(db)
	
if __name__ == "__main__":
	main_driver()