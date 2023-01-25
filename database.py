print("This is database.py") 
print("Python thinks this is called {}".format(__name__))
import new_func as nf
#import numpy as np 

HDL = 55 
HDL_analysis = nf.HDL_analysis(HDL)

print("The HDL analysis is {}".format(HDL_analysis))

nf.generic_input("Other Test") 