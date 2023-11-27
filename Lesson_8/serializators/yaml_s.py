import yaml

def yaml_serializator(person_list, n):
    with open(f'files/persons_{n}.yaml', 'w') as file:
        yaml_obj = [person.__dict__ for person in person_list]
        yaml.dump(yaml_obj, file)

    return f'files/persons_{n}.yaml'