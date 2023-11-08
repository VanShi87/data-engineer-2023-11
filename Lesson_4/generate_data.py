import string

import pandas as pd
import numpy as np
import faker

fake = faker.Faker()

NUM_PERSONS = 20
NUM_GROUPS = 5
NUM_FRIEND_LINKS = 30
NUM_GROUP_LINKS = 25
MAX_TWEETS = 10
MAX_CHAR = 15

df = pd.DataFrame()
df['sex'] = np.random.choice(['F', 'M'], NUM_PERSONS)
df['name'] = np.where(df['sex']=='F',
                      [fake.name_female() for _ in range(NUM_PERSONS)],
                      [fake.name_male() for _ in range(NUM_PERSONS)])
df['age'] = np.random.randint(16, 70, NUM_PERSONS)
df['city'] = np.random.choice(['Moscow', 'St-Petersburg', 'Voronezh', 'Yaroslavl', 'Sochi'], NUM_PERSONS)
df['tweets'] = [[fake.paragraph()[:np.random.randint(5, MAX_CHAR)]
                for _ in range(np.random.randint(0, MAX_TWEETS))]
               for _ in range(NUM_PERSONS)]
df['code'] = ('CREATE (:Person {name: "' +
               df['name'] +
              '", sex: "' +
               df['sex'] +
              '", age: ' +
               df['age'].astype('str') +
              ', city: "' +
              df['city'] +
              ', tweets: ' +
              df['tweets'].astype('str') +
              '});'
              )
df['code'] = df['code'].str.replace("u'", "'")

person_query = '\n'.join(df['code'].values)

df2 = pd.DataFrame()
df2['name'] = np.array(['football', 'pc games', 'chess', 'anime', 'horsing'])
df2['code'] = ('CREATE (:Group {name: "' +
               df2['name'] +
              '"});'
              )

group_query = '\n'.join(df2['code'].values)

df3 = pd.DataFrame()
df3['name1'], df3['name2'] = zip(*[np.random.choice(df['name'].values, size=2, replace=False)
                                   for _ in range(NUM_FRIEND_LINKS)])
df3['code'] = ('MATCH (p1:Person {name: "' +
                df3['name1'] +
               '"}), (p2:Person {name: "' +
                df3['name2'] +
               '"}) CREATE (p1)-[:Friend]->(p2);'
              )

friend_query = '\n'.join(df3['code'].values)

df4 = pd.DataFrame()
df4['person'] = np.random.choice(df['name'].values, size=25)
df4['group'] = np.random.choice(df2['name'].values, size=25)
df4['code'] = ('MATCH (p1:Person {name: "' +
                df4['person'] +
               '"}), (p2:Group {name: "' +
                df4['group'] +
               '"}) CREATE (p1)-[:Subscribe]->(p2);'
              )
subscribe_query = '\n'.join(df4['code'].values)

with open('commands.txt', 'a') as file:
    for query in (person_query, group_query, friend_query, subscribe_query):
        file.write(query + '\n')


