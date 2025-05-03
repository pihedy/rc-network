import serial
import time

from .base import SerialCommunication

class RealSerialCommunication(SerialCommunication):

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):
        self.serial = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

    def write(self, data: str) -> None:
        self.serial.write(data.encode())

    def read(self) -> str:
        return self.serial.readline().decode().strip()
