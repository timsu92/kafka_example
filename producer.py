import datetime
import asyncio
from random import randint
from time import sleep
from kafka import KafkaProducer
import kafka
from kafka.admin import NewTopic
from kafka.producer.future import FutureRecordMetadata, RecordMetadata
from kafka.protocol.admin import CreateTopicsResponse_v3

producer = KafkaProducer(bootstrap_servers='localhost:9092')
print("已啟動。用SIGINT (CTRL+C) 中止程式")

topic = "topic-test"

async def main():
    admin = kafka.KafkaAdminClient(bootstrap_servers=['localhost:9092'])
    topics = admin.list_topics()
    if topic not in topics:
        createResult: CreateTopicsResponse_v3 = admin.create_topics((NewTopic(topic, 2, 1),))  # type: ignore
        print(f"topic {topic} created")
    id = randint(0, 1000)
    i = 0
    try:
        while True:
            metadataFuture:FutureRecordMetadata = producer.send("topic-test", bytes(f"producer {id} sent {i}", "utf8"))
            metadata:RecordMetadata = metadataFuture.get() # type: ignore
            message = {
                    "topicName": metadata.topic,
                    "partition": metadata.partition,
                    "baseOffset": metadata.offset,
                    "logAppendTime": datetime.datetime.fromtimestamp(metadata.timestamp / 1000),
                    "logStartOffset": metadata.log_start_offset
                    }
            print(message)
            i += 1
            sleep(1)
    except KeyboardInterrupt:
        producer.close()
        

asyncio.run(main())
