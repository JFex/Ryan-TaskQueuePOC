# Ryan-TaskQueuePOC

## Requirements
- Python 3.7 or later
- Celery 5.2.*
- Redis server
- pyodbc Python module

## Starting the monitor
1. cd into the working environment
2. Execute the monitor.py file:
  `python .\monitor.py`

## Starting a celery worker instance:
1. cd into the working environment
2. Execute the following command:
  `python -m celery -A celeryproj worker --concurrency=5 --loglevel=INFO -P threads --task-events`
  NOTE: According to Celery documentation, Celery is not intended to be used in Windows environments. To get around that, we had to specify that the workers acheive concurrency with a thread pool instead of a processor pool.

## Starting the client to begin running tasks
1. cd into the working environment
2. Execute the client.py file:
  `python .\client.py`
