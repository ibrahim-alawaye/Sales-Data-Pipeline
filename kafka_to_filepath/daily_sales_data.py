import os
import json
import time
import pandas as pd
from confluent_kafka import Consumer, KafkaError
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()

kafka_config = {
    'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS'),
    'group.id': os.getenv('KAFKA_GROUP_ID'),
    'auto.offset.reset': 'earliest'
}


consumer = Consumer(kafka_config)
consumer.subscribe([os.getenv('KAFKA_TOPIC')])

def write_to_csv(data_list, file_path):
    df = pd.DataFrame(data_list)
    df.to_csv(file_path, index=False)


data_list = []
current_date = datetime.now().strftime('%Y%m%d')
folder_path = os.path.join("sales_data", current_date)

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_name = f"sales_data_{current_date}.csv"
file_path = os.path.join(folder_path, file_name)

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        
        # Add the record to the list
        record = json.loads(msg.value().decode('utf-8'))
        data_list.append(record)
        
        # Check if the date has changed
        new_date = datetime.now().strftime('%Y%m%d')
        if new_date != current_date:
            # Write the data to a new CSV file for the previous day
            write_to_csv(data_list, file_path)
            print(f"Data written to {file_path}")
            
            # Clear the data list
            data_list = []

            # Update the current date and file path
            current_date = new_date
            folder_path = os.path.join("sales_data", current_date)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_name = f"sales_data_{current_date}.csv"
            file_path = os.path.join(folder_path, file_name)

except KeyboardInterrupt:
    pass
finally:
    # Ensure remaining data is written to the final CSV file
    if data_list:
        write_to_csv(data_list, file_path)
        print(f"Data written to {file_path}")
    
    # Close Kafka consumer
    consumer.close()