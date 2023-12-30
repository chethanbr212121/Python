# Databricks notebook source
## Cretae data frames by tuple
ap_data=[(1,"Santosh"),(2,"Indu")]

# COMMAND ----------

ap_data_schema=["id","name"]

# COMMAND ----------

ap_list_tuple_df = spark.createDataFrame(data=ap_data, schema=ap_data_schema)

# COMMAND ----------

ap_list_tuple_df.show()

# COMMAND ----------

display(ap_list_tuple_df)

# COMMAND ----------

## Cretae data frames by dictionary
ap_data = [{"id":1,"name":"Santosh"}, {"id":2,"name":"Indu"}]

# COMMAND ----------

ap_dictionary_df = spark.createDataFrame(data=ap_data)

# COMMAND ----------

display(ap_dictionary_df)

# COMMAND ----------

ap_dictionary_df.printSchema()

# COMMAND ----------

## Create dataFrame with StructType and StructField (We can import two way difined below)
## from pyspark.sql.types import StrucType, StrucField, IntegerType, StringType 
from pyspark.sql.types import *

# COMMAND ----------

ap_data=[(1,"Santosh"),(2,"Indu")]

# COMMAND ----------

ap_data_schema = StructType([StructField(name="id", dataType=IntegerType()),
                             StructField(name="name", dataType=StringType())])

# COMMAND ----------

ap_StrucType_StrucField_df = spark.createDataFrame(data=ap_data, schema=ap_data_schema)

# COMMAND ----------

ap_StrucType_StrucField_df.show()

# COMMAND ----------

display(ap_StrucType_StrucField_df)

# COMMAND ----------

ap_StrucType_StrucField_df.printSchema()

# COMMAND ----------


