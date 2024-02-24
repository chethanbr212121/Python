from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Hello spark") \
        .master("local[3]") \
        .getOrCreate()
    print("Hello spark")
    df = spark.read.format("csv").option("header","true").option("inferSchema","True").load("/home/chethan/Documents/Documents/ETL/ETL_PRACTICE/SQL_Practice_Data/AdventureWorksCustomers.csv")
    df.show(10)
    df.printSchema()


    spark.stop()
