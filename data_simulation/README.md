# Sales Data Stream to Kafka

## Overview
This section describes how to stream sales data into a Kafka cluster using a Python program. The process involves setting up a Confluent Kafka environment using Docker Compose and streaming simulated sales data into Kafka in real-time.

## Steps to Stream Sales Data to Kafka

### Kafka and Confluent Setup
- We set up a Kafka cluster using Confluent services, including Zookeeper, Kafka Broker, and Schema Registry.
- The services are defined and orchestrated using Docker Compose.

### Data Simulation with Python
- A Python program (`sale_data.py`) is used to generate simulated sales data.
- The Python program streams this data into the Kafka cluster.
- The Python program is built into a Docker image and included in the Docker Compose setup.

### Docker Compose Configuration
- The `docker-compose.yml` file is configured to spin up the entire stack, including the Python data simulation service.
- The services are configured to depend on each other to ensure proper startup order.