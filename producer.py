from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
print("已啟動。用SIGINT (CTRL+C) 中止程式")
i = 0
try:
    while True:
        producer.send("topicName", bytes(f"{i}", "utf8"))
        i += 1
        sleep(1)
except KeyboardInterrupt:
    producer.close()
