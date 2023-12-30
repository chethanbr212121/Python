# Databricks notebook source
ap_csv_data = spark.read.csv(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers.csv", header=True, sep=",")
##/home/chethan/Documents/Documents/ETL/ETL_PRACTICE/SQL_Practice_Data/AdventureWorksCustomers.csv /data/
# COMMAND ----------

ap_csv_data.count()

# COMMAND ----------

ap_csv_data.printSchema()

# COMMAND ----------

ap_csv_data.show(20)

# COMMAND ----------

ap_csv_data = spark.read.csv(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers.csv", header=True, sep=",", inferSchema=True)

# COMMAND ----------

ap_csv_data.show(20)

# COMMAND ----------

ap_csv_data.printSchema()

# COMMAND ----------

ap_csv_data_1 = spark.read.format("csv").load(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers.csv", header=True)

# COMMAND ----------

ap_csv_data_1.printSchema()

# COMMAND ----------

ap_csv_data_1.show(20)

# COMMAND ----------

ap_csv_data_2 = spark.read.format("csv").load(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers.csv", header=True, sep=",")

# COMMAND ----------

ap_csv_data_2.show()

# COMMAND ----------

ap_csv_data_3 = spark.read.format("csv").load(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers.csv", header=True, sep="," , InferSchema=True)

# COMMAND ----------

ap_csv_data_3.printSchema()

# COMMAND ----------

ap_csv_data_3.show()

# COMMAND ----------


