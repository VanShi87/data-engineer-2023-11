import pickle
def native_serializator(person_list):
    with open('files/persons.pickle', 'wb') as file:
        pickle.dump(person_list, file)