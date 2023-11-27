import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
def parquet_serializator(person_list):
    person_df = pd.DataFrame([person.__dict__ for person in person_list])
    pq.write_table(pa.Table.from_pandas(person_df), 'files/person.parquet')
