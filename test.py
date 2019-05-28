from pyspark.sql import SparkSession
import json
import os


def look_up(o):
    """
    A mapping function that use a rainbow table to decrypt the medallion and hack_license.
    :param o: a spark row
    :return: the original data with the medallion and hack_license decrypted
    """

    medallion = o['medallion']
    hack_license = o['hack_license']

    # check medallion miss
    if medallion not in rainbow_table or hack_license not in rainbow_table:
        return o
    else:
        return rainbow_table[medallion], rainbow_table[hack_license], \
               o[2], o[3], o[4], o[5], o[6], o[7], o[8], o[9], o[10], o[11], o[12], o[13]


# load rainbow table from file
with open('rainbow.txt', 'r') as rainbow:
    rainbow_table = json.load(rainbow)

    # start a new spark session
    spark = SparkSession.builder \
        .master("local[1]") \
        .config("spark.executor.memory", "8g") \
        .config("spark.driver.memory", "8g") \
        .config("spark.memory.offHeap.enabled", True) \
        .config("spark.memory.offHeap.size", "8g") \
        .appName("MD5") \
        .getOrCreate()

    # load data from csv file
    df = spark.read.csv('trip_data_1.csv', header=True, samplingRatio=0.00000001).persist()

    # df.show(5, truncate=False)

    # decrypt medallion and hack_license
    ret = df.rdd \
        .map(lambda o: look_up(o)) \
        .saveAsTextFile(f'{os.getcwd()}/output')
