# Kafka Example for Python 3

This is a simple example of how to use Kafka with Python 3. It sends messages once a second and receive from the other side.

## Prerequisites

- Python 3
- Docker

## How to run

```bash
docker-compose up -d
mkdir kraft-persistence
# If you are using "rootful" docker, execute below:
chmod 777 kraft-persistence
```

Install Python dependencies:
```bash
pip install -r requirements.txt
```
Or install it with Poetry and activate virtual environment:
```bash
poetry install
poetry shell
```

Start producer:
```bash
python3 producer.py
```

Start consumer:
```bash
python3 consumer.py
```