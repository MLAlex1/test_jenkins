def transf_str(mystr:str) -> str:
	"""
	reverts and adds string to the original string
	"""
	mystr = mystr[::-1]
	mystr += "de"
	return mystr

def print_str(mystr:str):
	"""
	prints a given string
	"""
	print(mystr)