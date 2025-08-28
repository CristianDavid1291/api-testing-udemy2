import requests
from utilities.configurations import *
from utilities.resources import ApiResources

def test_add_student_data():
    url=get_config()['API']['base_url']
    response = requests.post(url= f"{url}/{ApiResources.ADD_NEW_STUDENT}",json=read_json("add_new_student.json"))
    print(response.status_code)
    print(response.json())

def test_get_student_data():
    url=get_config()['API']['base_url']
    response = requests.get(url= f"{url}/{ApiResources.ADD_NEW_STUDENT}/10681601",json=read_json("add_new_student.json"))
    print(response.status_code)
    print(response.json())

def test_update_student_data():
    url=get_config()['API']['base_url']
    response = requests.put(url= f"{url}/{ApiResources.ADD_NEW_STUDENT}/10681601",json=read_json("add_new_student.json"))
    print(response.status_code)
    print(response.json())

def test_delete_student_data():
    url=get_config()['API']['base_url']
    response = requests.put(url= f"{url}/{ApiResources.ADD_NEW_STUDENT}/10681601")
    print(response.status_code)
    print(response.json())



