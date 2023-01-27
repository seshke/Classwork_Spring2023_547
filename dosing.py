"""dosing.py
    Example program of calculating first-day dose of medicine for pediatric
        patients.
    NOTE:  This is a programming example, and should not be used for any
             type of medical treatment or diagnostics.
"""

def interface():
	keepRunning = True
	while keepRunning:
		print_dosing()
		diagnosis = int(input("Enter a number: "))
		
		print_weight()
		weight_input = input("Enter weight: ")
		
		dosage_mg_first_day,weight = analyze_weight(weight_input,diagnosis) 
		print_output(weight,dosage_mg_first_day)

def print_dosing():
	print("Day One Dosing Guidelines")
	print("")
	print("Choose diagnosis:")
	print("1 - Acute otitis media")
	print("2 - Acute bacterial sinusitis")
	print("3 - Community-acquired pneumonia")
	print("4 - Pharyngitis/tonsilitis")
		
def print_weight():
    print("PATIENT WEIGHT")
    print("Enter patient weight followed by units of kg or lb.")
    print("Examples:  65.3 lb      21.0 kg")
    
def analyze_weight(weight_input,diagnosis):
	weight_data = weight_input.split(" ")
	weight = float(weight_data[0])
	units = weight_data[1]
	if units == "lb":
		weight = weight / 2.205
	dosages_mg_per_kg = [30, 10, 10, 12]
	dosage_mg_per_kg = dosages_mg_per_kg[diagnosis-1]
	dosage_mg_first_day = weight * dosage_mg_per_kg
	return dosage_mg_first_day, weight
	
def print_output(weight, dosage_mg_first_day):
    print("CORRECT DOSAGE")
    print("For a patient weighing {:.1f} kg,".format(int(weight)))
    print("  the correct dosage is {:.1f} mg the first day".format(int(dosage_mg_first_day)))
		  
		  



if __name__ == '__main__':
    interface()
