import string

import pandas as pd
import numpy as np
import faker

fake = faker.Faker()
fake.ipv4()
fake.url()
fake.date_time_between('-30d')


def generate_random_integers(min_value, max_value, n):
    result = set()
    while len(result) < n:
        value = np.random.randint(min_value, max_value + 1)
        if value not in result:
            result.add(value)
    return np.fromiter(result, int)


def generate_duplicate_number_values(n, data_type, min_value, max_value, nonunique_percent):
    type_mapping = {int: generate_random_integers,
                    float: np.random.uniform}
    uniq_num = round(n * (1 - nonunique_percent / 100))
    if uniq_num == 0: uniq_num = 1
    uniq_values = type_mapping[data_type](min_value, max_value, uniq_num)
    dup_values = np.random.choice(uniq_values, size=n - uniq_num)
    all_values = np.concatenate([uniq_values, dup_values])
    return np.random.permutation(all_values)


def generate_duplicate_fake_values(n, data_type, nonunique_percent, args):
    global fake
    uniq_num = round(n * (1 - nonunique_percent / 100))
    uniq_values = [getattr(fake, data_type)(*args) for _ in range(uniq_num)]
    dup_values = np.random.choice(uniq_values, size=n - uniq_num)
    all_values = np.concatenate([uniq_values, dup_values])
    return np.random.permutation(all_values)


def generate_dataframe(n, columns):
    data = {}
    for column in columns:
        column_name, data_type, options = column
        min_value = options.get('minvalue', 0)
        max_value = options.get('maxvalue', 10 ** 18)
        nonunique_percent = options.get('nonunique', 0)
        str_length = options.get('length', None)
        format_template = options.get('format', '')
        args = options.get('args', [])

        if data_type in (int, float):
            values = generate_duplicate_number_values(n=n, data_type=data_type, min_value=min_value,
                                                      max_value=max_value, nonunique_percent=nonunique_percent)
        if data_type in ("ipv4", "url", "date_time_between"):
            values = generate_duplicate_fake_values(n=n, data_type=data_type, nonunique_percent=nonunique_percent,
                                                    args=args)

        data[column_name] = values

    return pd.DataFrame(data)


df = generate_dataframe(25, [('url', 'url', {'nonunique': 50}),
                             ('ip', 'ipv4', {'nonunique': 50}),
                             ('start_point', 'date_time_between', {'nonunique': 50, 'args': ['-30d']}),
                             ('duration', int, {'nonunique': 50, 'maxvalue': 3600})])
df.to_json('data.json', orient='values')
