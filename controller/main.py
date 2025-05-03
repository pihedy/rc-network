import time

from components.logger.log import setup_logger
from components.redis.listener import listener

import components.serial_comm.factory as serial_factory

logger = setup_logger('test')
serial = serial_factory.create_serial_communication()

logger.info("Starting controller...")

while True:
    listener(logger, serial)
    time.sleep(1)
