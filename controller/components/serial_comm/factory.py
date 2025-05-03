import os

from .base import SerialCommunication

from .mock_serial import MockSerialCommunication
from .real_serial import RealSerialCommunication

def create_serial_communication() -> SerialCommunication:
    mock = os.environ.get("CONTROLLER_MOCK_SERIAL", "false").lower() == "true"

    if mock:
        return MockSerialCommunication()

    return RealSerialCommunication()
