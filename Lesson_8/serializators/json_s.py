import json
def json_serializator(person_list):
    with open('files/persons.json', 'w') as file:
        json_obj = [person.__dict__ for person in person_list]
        json.dump(json_obj, file)