from pyhive import hive
import pandas as pd

def query_health_data():
    conn = hive.Connection(host='hive-metastore', port=10000, database='default')
    df = pd.read_sql("SELECT region, AVG(bmi) as avg_bmi FROM health_data GROUP BY region", conn)
    conn.close()
    return df.to_dict(orient='records')
