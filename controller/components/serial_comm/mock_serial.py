from .base import SerialCommunication

class MockSerialCommunication(SerialCommunication):

    def write(self, data: str) -> None:
        print(f"[MOCK SERIAL] >> {data.strip()}")

    def read(self) -> str:
        print("[MOCK SERIAL] << Reading dummy data")

        return "MOCK_RESPONSE"
