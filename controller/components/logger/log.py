import logging
import sys
import os

from datetime import datetime
from logging.handlers import TimedRotatingFileHandler

def setup_logger(name: str, debug: bool = False, log_dir: str = "log") -> logging.Logger:
    logger = logging.getLogger(name)

    date_str = datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(log_dir, f"{name.lower()}-{date_str}.log")

    stream_handler = logging.StreamHandler(sys.stdout)
    file_handler = TimedRotatingFileHandler(log_path, when="midnight", backupCount=7)

    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    stream_handler.setLevel(logging.DEBUG if debug else logging.INFO)
    file_handler.setLevel(logging.DEBUG if debug else logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    stream_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

    logger.propagate = False

    return logger

