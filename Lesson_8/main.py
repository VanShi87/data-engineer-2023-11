from generator import create_person_list
from serializators import *

person_list = create_person_list(2)
serializator_list = [avro_serializator, json_serializator, messagepack_serializator, native_serializator,
                     parquet_serializator, protobuffers_serializator, xml_serializator, yaml_serializator]

for serializator in serializator_list:
    if serializator is xml_serializator:
        serializator(person_list)