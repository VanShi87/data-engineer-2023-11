import msgpack

def messagepack_serializator(person_list):
    with open('files/persons.msgpack', 'wb') as file:
        msgpack_obj = [person.__dict__ for person in person_list]
        msgpack_data = msgpack.packb(msgpack_obj)
        file.write(msgpack_data)