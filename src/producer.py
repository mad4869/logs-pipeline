import time
from kafka import KafkaProducer
from kafka.errors import KafkaError


def produce_logs(
    kafka_server: str = "localhost:9092",
    topic: str = "logs",
    log_file: str = "access.log",
) -> None:
    """
    Produce logs to a Kafka topic from a log file.

    :param kafka_server: The Kafka server address.
    :param topic: The Kafka topic to which logs will be sent.
    :param log_file: The file from which logs will be read.
    :return: None
    :raises FileNotFoundError: If the log file does not exist.
    :raises KafkaError: If there is an error producing logs to Kafka.
    """
    producer = KafkaProducer(
        bootstrap_servers=kafka_server,
        value_serializer=lambda v: str(v).encode("utf-8"),
    )

    try:
        with open(log_file) as f:
            for line in f:
                producer.send(topic, value=line.strip())
                producer.flush()
                print(f"Produced log: {line.strip()}")
                time.sleep(0.1)
    except FileNotFoundError:
        print(f"Log file not found: {log_file}")
    except KafkaError as e:
        print(f"Error producing log: {e}")
    finally:
        producer.close()


if __name__ == "__main__":
    produce_logs(log_file="logs/nginx.log")
