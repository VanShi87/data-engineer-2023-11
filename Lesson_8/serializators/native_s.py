import pickle
def native_serializator(person_list, n):
    with open(f'files/persons_{n}.pickle', 'wb') as file:
        pickle.dump(person_list, file)
    return f'files/persons_{n}.pickle'