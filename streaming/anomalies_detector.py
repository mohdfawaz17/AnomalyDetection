import json
import random
import time
from datetime import datetime
import pytz
import csv

import numpy as np

from settings import TRANSACTIONS_TOPIC, DELAY, OUTLIERS_GENERATION_PROBABILITY
from utils import create_producer


def modify_record_to_represent_anomaly(record):
    """
    Modify the record to represent an anomaly.
    Here, we simply add a flag to the record indicating it's an anomaly.
    You can adjust this function based on your specific anomaly definition.
    """
    decoded_record = json.loads(record.decode("utf-8"))
    decoded_record["is_anomaly"] = True
    return json.dumps(decoded_record).encode("utf-8")


producer = create_producer()

if producer is not None:
    with open('Train_data.csv', 'r') as csv_file:
        for row in csv_file:
            # Split the row into individual JSON objects
            records = row.strip().split('\n')

            # Wrap the JSON objects in a list
            data = [json.loads(record) for record in records]
            json_data = json.dumps(data).encode("utf-8")

            # Simulate introducing anomalies with a certain probability
            if random.random() < OUTLIERS_GENERATION_PROBABILITY:
                # Modify the records to represent anomalies
                data = [modify_record_to_represent_anomaly(
                    record) for record in data]
                json_data = json.dumps(data).encode("utf-8")

            producer.produce(topic=TRANSACTIONS_TOPIC,
                             value=json_data,
                             key=None)
            producer.flush()

            time.sleep(DELAY)
