import os
import sys
import tempfile
from datetime import date, datetime
from pyspark.sql.functions import *

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, StringType

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyarrow import fs
# import pyarrow.parquet.encryption as pe
import pyspark.pandas as ps


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

    df = spark.read.csv('Taxi_Trips.csv', sep=',', header=True, inferSchema=True)

    # - Вывести динамику количества поездок помесячно
    (df.withColumn('Trip Start Timestamp', to_timestamp("Trip Start Timestamp", "MM/dd/yyyy hh:mm:ss a")).
     groupby(month('Trip Start Timestamp').alias('month')).count().sort('month', ascending=False).show())

    # - Вывести топ-10 компаний(company) по выручке(trip_total)
    df.groupby('company').agg(sum('Trip Total').alias('total_sum')).sort('total_sum', ascending=False).show(10)

    # - Подсчитать долю поездок < 5, 5 - 15, 16 - 25, 26 - 100 миль
    @udf(returnType=StringType())
    def categorizer(length):
        if not(length):
            return "NA"
        elif length < 5:
            return "Very short"
        elif length < 15:
            return "Short"
        elif length < 25:
            return "Medium"
        else:
            return "Long"

    total = df.count()
    trip_agg = (df.withColumn('Trip Length', categorizer(col('Trip Miles'))).filter(col('Trip Length')!='NA').
                groupby('Trip Length').count())
    trip_agg.withColumn('Percent', col('count')/total *100).show()

