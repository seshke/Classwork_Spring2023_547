import requests
import json
'''
r = requests.get("https://api.github.com/repos/seshke/Classwork_Spring2023_547/branches")
print(r)
print(type(r))
print(r.status_code)
branches = r.json()
print(branches)

out_data = {"name": "aleks k", "net_id": "ak559"}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json = out_data)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/ak559")
print(r.text)
'''
URL = "http://vcm-7631.vm.duke.edu:5002/"
r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_patients/ak559')
print(r.text)
r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4')
print(r.text)
r = requests.get('http://vcm-7631.vm.duke.edu:5002/get_blood_type/M8')
print(r.text)

out_data = {"Name": "ak559", "Match": "Yes"}
r = requests.post(URL + "match_check", json = out_data)
print(r.text)