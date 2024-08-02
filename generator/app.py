# generator/app.py

from kafka import KafkaProducer
# from confluent_kafka import Producer
import os
from time import sleep
from transactions import create_random_transaction
import json

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
TRANSACTIONS_TOPIC = os.environ.get("TRANSACTIONS_TOPIC")
TRANSACTIONS_PER_SECOND = float(os.environ.get("TRANSACTIONS_PER_SECOND"))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND

if __name__ == "__main__":
    
    # producer = Producer(
    #     'bootstrap.servers':KAFKA_BROKER_URL,
    #     value_serializer=lambda value: json.dumps(value).encode()
    # )

    # Create the Producer instance
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
    }
    producer = KafkaProducer(producer_config)

    # 'bootstrap.servers':KAFKA_BROKER_URL, value_serializer=lambda value: json.dumps(value).encode()
    while True: 
        # transaction: dict = create_random_transaction()
        transaction = create_random_transaction()
        # Kafka messages are plain bytes => need to `.encode()` the string message 
        # Serialize the transaction to JSON
        serialized_transaction = json.dumps(transaction).encode('utf-8')
        producer.produce(TRANSACTIONS_TOPIC, value=serialized_transaction)
        producer.flush()
        # producer.send("queueing.transactions", value=transaction) 
        print(transaction) # DEBUG
        sleep(SLEEP_TIME) # Sleep for one second before producing the next transaction
