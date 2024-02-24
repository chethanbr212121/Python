# Databricks notebook source
employee_data = [(10,"Raj","1999","100","M",2000),
                 (20,"Rahul","2002","200","M",8000),
                 (30,"Raghu","2018","100","",6000),
                 (40,"Rama","2004","100","F",7000),
                 (50,"Rashi","2008","400","F",1000),
                 (60,"Rasul","2004","500","M",5000)]

# COMMAND ----------

employee_schema = ["employee_id","name","dob","employee_dept_id","gender","salary"]

# COMMAND ----------

employeeDf = spark.createDataFrame(data=employee_data, schema=employee_schema)

# COMMAND ----------

employeeDf.show()

# COMMAND ----------

department_data = [("HR",100),
                   ("Supply",200),
                   ("Sales",300),
                   ("Stock",400)]

# COMMAND ----------

drpartment_schema = ["dept_name","dept_id"]

# COMMAND ----------

departmentDF = spark.createDataFrame(data=department_data, schema=drpartment_schema)

# COMMAND ----------

departmentDF.show()

# COMMAND ----------

inner_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "inner")

# COMMAND ----------

inner_joinDF.show()

# COMMAND ----------

full_outer_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "full_outer")

# COMMAND ----------

full_outer_joinDF.show()

# COMMAND ----------

left_outer_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "left_outer")

# COMMAND ----------

left_outer_joinDF.show()

# COMMAND ----------

right_outer_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "right_outer")

# COMMAND ----------

right_outer_joinDF.show()

# COMMAND ----------

#Gives only matching data like "inner join" but results contain only left df columns.

left_semi_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "left_semi")

# COMMAND ----------

left_semi_joinDF.show()

# COMMAND ----------

#Gives only non matching data from left df and results contain only left df columns.

left_anti_joinDF = employeeDf.join(departmentDF, employeeDf.employee_dept_id == departmentDF.dept_id, "left_anti")

# COMMAND ----------

left_anti_joinDF.show()


# COMMAND ----------


