from pyspark.sql import SparkSession
import json
import os

spark = SparkSession.builder \
        .master("local[1]") \
        .config("spark.executor.memory", "8g") \
        .config("spark.driver.memory", "8g") \
        .config("spark.memory.offHeap.enabled", True) \
        .config("spark.memory.offHeap.size", "8g") \
        .appName("MD5") \
        .getOrCreate()

# load data
df = spark.read.csv('trip_data_1.csv', header=True, samplingRatio=0.00000001)

# df.rdd.saveAsTextFile(os.getcwd() + '/' + 'output')

df.toPandas.to_csv('sample.csv')
