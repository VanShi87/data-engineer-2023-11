import avro.schema
from avro.datafile import DataFileWriter
from avro.io import DatumWriter

avro_schema = avro.schema.parse('''
                                {
                                    "type": "record",
                                    "name": "Person",
                                    "fields": [
                                        {"name": "name", "type": "string"},
                                        {"name": "interests", "type": {"type": "array", "items": "string"}},
                                        {"name": "projectToHours", "type": {"type": "map", "values": "int"}},
                                        {"name": "age", "type": "int"},
                                        {"name": "salary", "type": "float"}
                                    ]
                                }
                                ''')

def avro_serializator(person_list):
    avro_writer = DataFileWriter(open('files/person.avro', 'wb'), DatumWriter(), avro_schema)
    for person in person_list:
        avro_writer.append(person.__dict__)
    avro_writer.close()