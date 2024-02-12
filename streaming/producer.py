import json
import random
import time
from datetime import datetime
import pytz
import csv

import numpy as np

from settings import TRANSACTIONS_TOPIC, DELAY, OUTLIERS_GENERATION_PROBABILITY
from utils import create_producer

producer = create_producer()

if producer is not None:
    with open('Train_data.csv', 'r') as csv_file:
        for row in csv_file:
            record = row.strip().encode("utf-8")

            producer.produce(topic=TRANSACTIONS_TOPIC,
                             value=record,
                             key=None)
            producer.flush()

            time.sleep(DELAY)
