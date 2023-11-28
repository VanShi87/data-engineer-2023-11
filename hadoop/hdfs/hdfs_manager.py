import pandas as pandas
from hdfs3 import HDFileSystem

# hdfs3, is a lightweight Python wrapper around the C/C++ libhdfs3 library.
# It provides both direct access to libhdfs3 from Python as well as a typical Pythonic interface
# https://hdfs3.readthedocs.io/en/latest/

host = 'localhost'
port = 8022
user = 'cloudera'

# hdfs = HDFileSystem(host='localhost', port=8020)
hdfs = HDFileSystem(host, port, user)

hdfs.ls('/user/data')
hdfs.put('file.txt', 'file.txt')
hdfs.cp('file.txt', '/user/data')

with hdfs.open('/user/data/file.txt', 'rb') as f:
    data = f.read(1000000)

with hdfs.open('/user/data/file.csv.gz') as f:
    df = pandas.read_csv(f, compression='gzip', nrows=1000)