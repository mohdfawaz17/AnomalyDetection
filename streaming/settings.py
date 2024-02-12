import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DELAY = 2
NUM_PARTITIONS = 3
OUTLIERS_GENERATION_PROBABILITY = 0.2
KAFKA_BROKER = "localhost:9092"
TRANSACTIONS_TOPIC = "transactions"
TRANSACTIONS_CONSUMER_GROUP = "transactions"
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"

SLACK_API_TOKEN = "xoxb-6143560644048-6272752675415-QqpTD1dcxEOU3CFlWlYIw4nB"
SLACK_CHANNEL = "C068HN5F77E"