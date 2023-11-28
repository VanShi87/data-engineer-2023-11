import sys
def mapper(line):
    value, groups_str = line.split()
    groups = groups_str.split(',')
    unique_values = {}
    for group in groups:
        if group in unique_values:
            unique_values[group] += 1
        else:
            unique_values[group] = 1
    for key, count in unique_values.items():
        print(f'{value},{key} {count}')

for line in sys.stdin:
    mapper(line)