# This is a sample Python script.
import os
import sys
import tempfile
from datetime import date, datetime
from pyspark.sql.functions import *

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs
# import pyarrow.parquet.encryption as pe
import pyspark.pandas as ps


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    os.environ['PYSPARK_PYTHON'] = sys.executable
    os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

    conf = SparkConf().setAppName("rddExample").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    print("spark.version=", sc.version)

    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("wordsCount") \
        .getOrCreate()

    # df = spark.read.csv('winemag-data-130k-v2.csv', sep=',', header=True, inferSchema=True)
    # filteredDF = df.filter(col('country').isNotNull()).filter(col('price').cast(DoubleType()).isNotNull())
    # filteredDF.groupby(col('country')).agg(max('price').alias('max_price')).sort('max_price', ascending=False).show(10)
    # filteredDF.show(10)
    df = spark.read.text('words.txt')
    df.select(explode(split(col("value"), "\s+")).alias("word")).groupby('word').count().show()

