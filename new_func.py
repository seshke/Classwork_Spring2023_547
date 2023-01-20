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

interface()