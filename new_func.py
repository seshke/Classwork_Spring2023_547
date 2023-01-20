def interface():
	print("Blood Calculator")
	keep_running = True
	while keep_running:
		print("Options")
		print("9- Quit")
		choice = input("Select and option:")
		if choice == "9":
			keep_running =False
			return
		print("Program Ending")
		
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

interface()