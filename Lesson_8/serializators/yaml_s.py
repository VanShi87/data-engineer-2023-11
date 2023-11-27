import yaml

def yaml_serializator(person_list):
    with open('files/persons.yaml', 'w') as file:
        yaml_obj = [person.__dict__ for person in person_list]
        yaml.dump(yaml_obj, file)