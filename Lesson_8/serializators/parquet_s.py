import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
def parquet_serializator(person_list, n):
    person_df = pd.DataFrame([person.__dict__ for person in person_list])
    person_df.to_parquet(f'files/persons_{n}.parquet')
    # pq.write_table(pa.Table.from_pandas(person_df), f'files/persons_{n}.parquet')

    return f'files/persons_{n}.parquet'