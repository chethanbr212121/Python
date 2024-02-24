from pyspark.sql import *

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Hello spark") \
        .master("local[3]") \
        .getOrCreate()
    print("Hello spark")
"""
## Create data frame.
df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (23, "Alice")], schema=["age", "name"])

df.show()
print(df.distinct().count()) """



"""
## Create temp table and ue sl for data manipulaton.
df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])

df.createGlobalTempView("people")

df2.show()

df2 = spark.sql("SELECT * FROM global_temp.people where age='2'")

df2.show() """


"""
## Select columns operations.
df = spark.createDataFrame([

    (2, "Alice"), (5, "Bob")], schema=["age", "name"])

df.select(df.age).show()

df.select(df['age']).show()

df.select(df[1]).show()

df[["name", "age"]].show()

df[df.age > 3].show()

df[df[0] > 3].show() """

##


