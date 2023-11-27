import json
def json_serializator(person_list, n):
    with open(f'files/persons_{n}.json', 'w') as file:
        json_obj = [person.__dict__ for person in person_list]
        json.dump(json_obj, file)

    return f'files/persons_{n}.json'