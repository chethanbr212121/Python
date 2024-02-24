# Databricks notebook source
filter_df = spark.read.format("csv").load(path="dbfs:/FileStore/shared_uploads/chethanbr212@gmail.com/AdventureWorksCustomers-1.csv", header=True, sep=",", Inferschema=True)

# COMMAND ----------

filter_df.show(20)

# COMMAND ----------

Df_1 = filter_df.filter(filter_df.Gender=="M")

# COMMAND ----------

Df_1.count()

# COMMAND ----------

df_2 = filter_df.filter(filter_df.TotalChildren >= 2)

# COMMAND ----------

df_2.show(5)

# COMMAND ----------

df_3 = filter_df.filter(filter_df.FirstName.contains("EUGENE"))

# COMMAND ----------

df_3.show()

# COMMAND ----------

df_4 = filter_df.filter(filter_df.TotalChildren != 5)

# COMMAND ----------

df_4.show()

# COMMAND ----------

df_5 = filter_df.filter((filter_df.TotalChildren >= 2) & (filter_df.TotalChildren <= 4) )

# COMMAND ----------

df_5.count()

# COMMAND ----------

df_6 = filter_df.filter((filter_df.TotalChildren >= 2) | (filter_df.TotalChildren <= 4) )

# COMMAND ----------

df_6.count()

# COMMAND ----------

df_7 = filter_df.filter(filter_df.EducationLevel.isNull())

# COMMAND ----------

df_7.count()

# COMMAND ----------

df_8 = filter_df.filter(filter_df.EducationLevel.isNotNull())

# COMMAND ----------

df_8.count()

# COMMAND ----------

df_9 = filter_df.filter(filter_df.Occupation.like('%Prof%'))

# COMMAND ----------

df_new_9 = filter_df.filter(filter_df.Occupation.like('Prof%'))

# COMMAND ----------

df_new_9.show(5)

# COMMAND ----------

df_9.count()

# COMMAND ----------

df_10 = filter_df.filter(filter_df.TotalChildren.isin(2,0,4))

# COMMAND ----------

df_10.count()

# COMMAND ----------

df_11 = filter_df.filter(filter_df.LastName.startswith("CHE"))

# COMMAND ----------

df_11.show(5)

# COMMAND ----------

df_12 = filter_df.filter(filter_df.LastName.endswith("LE"))

# COMMAND ----------

df_12.show(5)

# COMMAND ----------


