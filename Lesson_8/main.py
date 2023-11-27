import time
import os
from itertools import chain

import pandas as pd
import numpy as np

from generator import create_person_list
from serializators import *

serializator_list = [avro_serializator, json_serializator, messagepack_serializator, native_serializator,
                     parquet_serializator, protobuffers_serializator, xml_serializator, yaml_serializator]

num_rows = [1000, 10000, 100000]
df = pd.DataFrame(data=np.zeros((len(serializator_list), len(num_rows)*2)),
                  index=[str(serializator).split()[1].split('_')[0] for serializator in serializator_list],
                  columns=list(chain(*[(f"n={n}, time, s", f"n={n}, volume, Kb") for n in num_rows])))

for n in num_rows:
    person_list = create_person_list(n)
    for serializator in serializator_list:
        if n>10000 and serializator is parquet_serializator:
            continue
        start = time.time()
        file = serializator(person_list, n)
        end = time.time()
        index = str(serializator).split()[1].split('_')[0]
        df.loc[index, f"n={n}, time, s"] = (end - start)
        df.loc[index, f"n={n}, volume, Kb"] = os.path.getsize(file)/1024
        print(n, index)
df.to_excel('statistics.xlsx')