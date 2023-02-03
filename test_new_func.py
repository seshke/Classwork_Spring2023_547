import pytest

@pytest.mark.parametrize("HDL_input, expected",
[(65,"Normal"),(45,"Borderline Low"),(20,"Low")])
def test_HDL_analysis(HDL_input, expected):
	from new_func import HDL_analysis
	# Arrange
	# Act 
	answer = HDL_analysis(HDL_input)
	# Assert
	assert answer == expected 
	
@pytest.mark.parametrize("LDL_input, expected",
[(200,"Very High"),(170,"High"),(140,"Borderline High"),(20,"Normal")])
def test_LDL_analysis(LDL_input, expected):
	from new_func import LDL_analysis
	# Arrange
	# Act 
	answer = LDL_analysis(LDL_input)
	# Assert
	assert answer == expected 
	
def test_check_fever():
	from new_func import check_fever
	input_temps = [97, 98.6, 100.1, 103, 98.4]
	answer = check_fever(input_temps)
	expected = True
	assert answer == expected 
	

def check_fever(input_list):
	for temp in input_list:
		if temp > 100.5:
			return True
	return False 
