from sqlalchemy import create_engine
import clickhouse_driver
import pandas as pd

df = pd.read_csv('titanic.csv')
conn = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
df.to_sql('titanic', conn, if_exists='replace', index=False, method='multi')

with clickhouse_driver.connect(host='localhost', port=9000) as conn:
    with conn.cursor() as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS titanic ('
                   'PassengerId Int64,'
                   'Survived Int64,'
                   'Pclass Int64,'
                   'Name String,'
                   'Sex String,'
                   'Age Float64,'
                   'SibSp Int64,'
                   'Parch Int64,'
                   'Ticket String,'
                   'Fare Float64,'
                   'Cabin String,'
                   'Embarked String'
                   ') ENGINE = MergeTree() ORDER BY PassengerId')


        export_query = '''
        INSERT INTO titanic 
        SELECT *
        FROM "postgresql"('127.0.0.1:5432', 'postgres', 'titanic', 'postgres', 'postgres')
        '''

        cursor.execute(export_query)




