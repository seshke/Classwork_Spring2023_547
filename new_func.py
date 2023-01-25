def interface():
	print("Blood Calculator")
	keep_running = True
	while keep_running:
		print("Options")
		print("1- HDL")
		print("2 - LDL")
		print("9- Quit")
		choice = input("Select and option:")
		if choice == "9":
			keep_running =False
		elif choice == "1":
			HDL_driver()
		elif choice == "2":
			LDL_driver()
		
	print("Program Ending")

def HDL_driver():
	HDL_in = HDL_input()
	HDL_analy = HDL_analysis(HDL_in) 
	HDL_output(HDL_in,HDL_analy)
		
def HDL_input():
	HDL_value = input("Enter HDL result:")
	HDL_value = int(HDL_value)
	return HDL_value
	
def HDL_analysis(HDL_int): 
	if HDL_int >= 60:
		answer = "Normal"
	elif 40 <= HDL_int < 60: 
		answer = "Borderline Low" 
	else: 
		answer = "Low"
	return answer 
	
def HDL_output(HDL_value,HDL_analy):
	print("The HDL result of {} is considered {}".format(HDL_value,HDL_analy))
	
def LDL_analysis(LDL_int):
	if LDL_int >= 190:
		answer = "Very High"
	elif 160<= LDL_int < 190:
		answer = "High"
	elif 130<= LDL_int < 160:
		answer = "Borderline High"
	else:
		answer = "Normal"
	return answer 
	
def LDL_driver():
	LDL_in = LDL_input()
	LDL_analy = LDL_analysis(LDL_in) 
	LDL_output(LDL_in,LDL_analy)
		
def LDL_input():
	LDL_value = input("Enter LDL result:")
	LDL_value = int(LDL_value)
	return LDL_value
	
def LDL_output(LDL_value,LDL_analy):
	print("The LDL result of {} is considered {}".format(LDL_value,LDL_analy))


def chol_analysis(chol_int):
	if chol_int >= 240:
		answer = "High"
	elif 200 <= chol_int < 239:
		answer = "Borderline High"
	else:
		answer = "Normal"
	return answer 
	
def chol_driver():
	chol_in = chol_input()
	chol_analy = chol_analysis(chol_in) 
	chol_output(chol_in,chol_analy)
		
def chol_input():
	chol_value = input("Enter Cholesterol result:")
	chol_value = int(chol_value)
	return chol_value
	
def LDL_output(chol_value,chol_analy):
	print("The Cholesterol result of {} is considered {}".format(chol_value,chol_analy))


interface()