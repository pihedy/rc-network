import os
import time
import serial

def run_serial_controller():
    port = os.environ.get("SERIAL_PORT", "/dev/ttyUSB0")
    baud = int(os.environ.get("SERIAL_BAUDRATE", 115200))
    
    try:
        ser = serial.Serial(port, baud, timeout=1)
        print(f"[serial_controller] Connected to {port} at {baud} baud")
    except Exception as e:
        print(f"[serial_controller] Failed to connect to serial: {e}")
        return

    while True:
        try:
            if ser.in_waiting:
                line = ser.readline().decode(errors="ignore").strip()
                print(f"[serial] {line}")
        except Exception as e:
            print(f"[serial_controller] Error during serial read: {e}")
            break

        time.sleep(0.1)
