from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

def process_health_data():
    spark = SparkSession.builder \
        .appName("Health Data Processor") \
        .getOrCreate()

    df = spark.read.csv("data/health_data.csv", header=True, inferSchema=True)

    avg_bmi_by_region = df.groupBy("region").agg(avg("bmi").alias("avg_bmi"))
    avg_charges_by_smoker = df.groupBy("smoker").agg(avg("charges").alias("avg_charges"))

    bmi_result = avg_bmi_by_region.toPandas().to_dict(orient="records")
    charge_result = avg_charges_by_smoker.toPandas().to_dict(orient="records")

    return {"bmi_by_region": bmi_result, "charges_by_smoker": charge_result}
