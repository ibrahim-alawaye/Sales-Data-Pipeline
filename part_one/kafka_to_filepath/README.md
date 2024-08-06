# Kafka to CSV Data Pipeline

This project reads sales data from a Kafka topic and saves the data into CSV files. The data is organized into daily folders, with a new CSV file created each day. The infrastructure for this process includes Kafka brokers, Zookeeper, Confluent, and other necessary components, managed through Docker Compose.



## Description

1. **Kafka to CSV Conversion**: The `daily_sales_data.py` script reads sales data from a Kafka topic, converts the data to CSV format using Pandas, and saves it in a specified file path. The data is saved in daily folders.

2. **Docker Compose**: The Docker Compose file (`docker-compose.yml`) sets up the entire infrastructure, including Kafka brokers, Zookeeper, and Confluent components. The script listens to sales data coming from Kafka and processes it accordingly.

3. **Environment Variables**: All configurations, including Kafka and MySQL connection details, are stored in environment variables. These variables are loaded from a `.env` file before execution.

KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_GROUP_ID=my_group
KAFKA_TOPIC=sales_topic
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_DATABASE=your_database


## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Steps

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd kafka_to_csv

