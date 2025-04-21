import time

def run_mock_serial():
    print("[mock_serial] Mock mode active — no serial device")
    counter = 0
    while True:
        print(f"[mock_serial] Simulated input {counter}")
        counter += 1
        time.sleep(5)
