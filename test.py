from pyspark.sql import SparkSession
import pandas as pd

rainbow = pd.read_csv('rainbow.csv', names=['hash', 'string'], low_memory=True)


print(rainbow)

# print(rainbow.loc('89D227B655E5C82AECF13C3F540D4CF4'))
#
#
# def look_up(o):
#     o['medallion'] = rainbow.loc[o['medallion']]
#     o['hack_license'] = rainbow.loc[o['hack_license']]
#     return o


# spark = SparkSession.builder \
#         .master("local[*]") \
#         .appName("Word Count") \
#         .getOrCreate()
#
# df = spark.read.csv('trip_data_1.csv', header=True)
#
# df.show(5, truncate=False)
# sample = df.sample(0.0001)
# ret = sample.rdd.map(lambda o: look_up(o)).take(5)
# [print(o) for o in ret]



