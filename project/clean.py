from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CleanTransactions").getOrCreate()
df = spark.read.option("header", "true").csv("gs://eswar-bucket/sample_transaction_data.csv")
clean_df = df.dropna().filter("transaction_id != ''")
failed_txns = clean_df.filter(clean_df.transaction_status == 'FAILED')
failed_txns.write.csv("gs://eswar-bucket/cleaned_transactions", header=True)
