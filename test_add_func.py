import pytest

def test_add():
	from add_func import add
	answer = add(1.1,0.2)
	assert answer == 1.3