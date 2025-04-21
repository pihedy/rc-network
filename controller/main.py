import os
from serial_controller import run_serial_controller
from mock_serial import run_mock_serial

mock = os.environ.get("CONTROLLER_MOCK_SERIAL", "false").lower() == "true"

if mock:
    run_mock_serial()
else:
    run_serial_controller()
