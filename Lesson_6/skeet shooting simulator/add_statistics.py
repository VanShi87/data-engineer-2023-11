import json

import pandas as pd
import clickhouse_driver

df_list = []
with open('statistics.json') as file:
    for line in file:
        json_dict = json.loads(line)
        session = list(json_dict.keys())[0]
        data = [value for value in json_dict.values()][0]
        df = pd.DataFrame(columns=['mouse_position_x', 'mouse_position_y', 'mouse_click', 'time_stamp', 'score', 'bullets'], data=data)
        df['session_id'] = session
        df_list.append(df)

df_all = pd.concat(df_list)

with clickhouse_driver.connect(host='localhost', port=9000) as conn:
    with conn.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS sss_statistics ('
                   'mouse_position_x Int64,'
                   'mouse_position_y Int64,'
                   'mouse_click Int64,'
                   'time_stamp Float64,'
                   'score Int64,'
                   'bullets Int64,'
                   'session_id String'
                   ') ENGINE = MergeTree() ORDER BY session_id')


client = clickhouse_driver.Client(host='localhost', port=9000, settings={'use_numpy': True})
client.insert_dataframe(f'INSERT INTO sss_statistics VALUES', df_all)