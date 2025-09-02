import requests
from utilities.configurations import *
from utilities.resources import ApiResources

def test_add_student_data():
    url=get_config()['API']['base_url']
    response = requests.post(url= f"{url}/{ApiResources.ADD_NEW_PET}",json=read_json("add_new_pet.json"))
    assert response.status_code == 200

def test_get_student_by_status():
    url=get_config()['API']['base_url']
    response = requests.get(url= f"{url}/{ApiResources.GET_BY_STATUS}",headers={"Accept": "application/json"} ,params={"status": "available"})
    assert response.status_code == 200



