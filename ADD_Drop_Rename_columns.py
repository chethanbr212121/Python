# Databricks notebook source
df_1 = spark.read.format("csv").load(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers-1.csv", header=True, sep=",", Inferschema=True)

# COMMAND ----------

df_1.show(5)

# COMMAND ----------

## Import lit to add columns
from pyspark.sql.functions import lit

# COMMAND ----------

df_add_column = df_1.withColumn("Location",lit("Mumbai"))

# COMMAND ----------

df_add_column.show(5)

# COMMAND ----------

df_add_column_1 = df_1.withColumn("MinusChild",df_1.TotalChildren-1)

# COMMAND ----------

df_add_column_1.show(5)

# COMMAND ----------

## Import below functions to concate
from pyspark.sql.functions import concat,col

# COMMAND ----------

## ADD lit(" ") to add space between first and last names.
df_add_column_2 = df_1.withColumn("FullName",concat(df_1.FirstName,lit(" "),df_1.LastName))

# COMMAND ----------

df_add_column_2.show(5)

# COMMAND ----------

## Rename EmailAddress to Email
df_rename = df_1.withColumnRenamed("EmailAddress","Email")

# COMMAND ----------

df_rename.show(5)

# COMMAND ----------

## Multiple column rename
df_rename_1 = df_1.withColumnRenamed("EmailAddress","Email").withColumnRenamed("BirthDate","DOJ")

# COMMAND ----------

df_rename_1.show(5)

# COMMAND ----------

df_dropcolumn = df_1.drop("Prefix").drop("LastName")

# COMMAND ----------

df_dropcolumn.show(5)

# COMMAND ----------

df_1.count()


# COMMAND ----------

df_3 = df_1

# COMMAND ----------

df_3.count()

# COMMAND ----------

df_union = df_1.union(df_3)

# COMMAND ----------

df_union.count()

# COMMAND ----------

df_nodup = df_union.dropDuplicates()

# COMMAND ----------

df_nodup.count()


# COMMAND ----------


