import redis
import json
import logging

from components.serial_comm.base import SerialCommunication

def listener(logger: logging.Logger, serial: SerialCommunication, channel: str = 'car/commands'):
    try:
        logger.info(f"Listening on channel: {channel}")

        redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

        pubsub = redis_client.pubsub()
        pubsub.subscribe(channel)

        for message in pubsub.listen():
            logger.info(f"Received message: {message}")

            if message['type'] != 'message':
                continue

            logger.info(f"Received message: {message['data']}")
            serial.write(message['data'])
    except Exception as e:
        logger.error(f"Error in listener: {e}")
