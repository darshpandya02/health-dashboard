# from pyspark.sql import SparkSession
# from pyspark.sql.functions import avg

# def process_health_data():
#     spark = SparkSession.builder \
#         .appName("Health Data Processor") \
#         .getOrCreate()

#     df = spark.read.csv("data/health_data.csv", header=True, inferSchema=True)

#     avg_bmi_by_region = df.groupBy("region").agg(avg("bmi").alias("avg_bmi"))
#     avg_charges_by_smoker = df.groupBy("smoker").agg(avg("charges").alias("avg_charges"))

#     bmi_result = avg_bmi_by_region.toPandas().to_dict(orient="records")
#     charge_result = avg_charges_by_smoker.toPandas().to_dict(orient="records")

#     return {"bmi_by_region": bmi_result, "charges_by_smoker": charge_result}

# spark_processor.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, FloatType

spark = SparkSession.builder \
    .appName("KafkaToHive") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .enableHiveSupport() \
    .getOrCreate()

schema = StructType() \
    .add("patient_id", IntegerType()) \
    .add("age", IntegerType()) \
    .add("gender", StringType()) \
    .add("bmi", FloatType()) \
    .add("smoker", StringType()) \
    .add("region", StringType()) \
    .add("charges", FloatType())

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "health-topic") \
    .load()

# Extract and parse JSON
health_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Write to Hive Table
query = health_df.writeStream \
    .outputMode("append") \
    .format("hive") \
    .option("checkpointLocation", "/tmp/health_checkpoint") \
    .option("path", "/user/hive/warehouse/health_data") \
    .table("health_data") \
    .start()

query.awaitTermination()
