import msgpack

def messagepack_serializator(person_list, n):
    with open(f'files/persons_{n}.msgpack', 'wb') as file:
        msgpack_obj = [person.__dict__ for person in person_list]
        msgpack_data = msgpack.packb(msgpack_obj)
        file.write(msgpack_data)
    return f'files/persons_{n}.msgpack'