from flask import Flask, request, jsonify

db = {}
app = Flask(__name__)

def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type, 
                   "tests" : []}
    db[id] = new_patient
    print(db)

@app.route("/new_patient", methods= ["POST"])
def post_new_patient():
    in_data = request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer), status_code


def new_patient_driver(in_data):
    validation = validate_input_data(in_data)
    if not validation:
        return validation, 400
    add_patient_to_db(in_data["id"], in_data['name'], in_data['blood_type'])
    return "Patient added!", 200


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ['name','id','blood_type']
    expected_types = [str, int, str]
    for key,value in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value:
            return "Key {} has the incorrect value type".format(key)
    return True


def add_test_to_db(id, test_name, test_result):
    new_test = {"id": id,
                   "test_name": test_name,
                   "test_result": test_result}
    db[id] = new_test
    print(db)

@app.route("/add_test", methods= ["POST"])
def post_add_test():
    in_data = request.get_json()
    answer, status_code = add_test_driver(in_data)
    return jsonify(answer), status_code


def add_test_driver(in_data):
    validation = validate_input_test(in_data)
    if not validation:
        return validation, 400
    add_patient_to_db(in_data["id"], in_data['test_name'], in_data['test_result'])
    return "Test added!", 200


def validate_input_test(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ['id','test_name','test_result']
    expected_types = [int, str, int]
    for key,value in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value:
            return "Key {} has the incorrect value type".format(key)
    return True

if __name__=='__main__':
    app.run()