import time
from generator import create_person_list
from serializators import *

person_list = create_person_list(2)
serializator_list = [avro_serializator, json_serializator, messagepack_serializator, native_serializator,
                     parquet_serializator, protobuffers_serializator, xml_serializator, yaml_serializator]

for n in (1000, 10000, 100000):
    for serializator in serializator_list:
        start = time.time()
        file = serializator(person_list, n)
        end = time.time()