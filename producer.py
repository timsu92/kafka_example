import datetime
import asyncio
from random import randint
from time import sleep
from kafka import KafkaProducer
from kafka.producer.future import FutureRecordMetadata, RecordMetadata

producer = KafkaProducer(bootstrap_servers='localhost:9092')
print("已啟動。用SIGINT (CTRL+C) 中止程式")

async def main():
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
