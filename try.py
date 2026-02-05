from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("getnam").getOrCreate()
print("hello")
spark.stop()
