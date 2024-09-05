
from py_canoe import CANoe
import time

class MockedECUCANoe(CANoe):
    def __init__(self, id_, channel, bus):
        super().__init__()  # Initialize the parent class (CANoe)
        self._id = id_
        self._canoe_cfg = r'C:\Users\viktoriia.taraniuk\PycharmProjects\Udemy\CANoe\pythonProject1\CANoe_test\CAN_500kBaud_1ch.cfg'
        self._channel = 1
        self._bus = 'CAN'
        self._on = False
        self._raw_data = None

    def power_on_canoe(self):
        self.open(self._canoe_cfg)
        self.start_measurement()
        self._on = True

    def get_signal_value_canoe(self, bus, channel, message, signal, raw_value=True):
        sig_val = self.get_signal_value(bus, channel, message, signal, raw_value)
        return sig_val

    def power_off_canoe(self):
        self.stop_measurement()
        self.quit()
        self._on = False

    def raw_data(self):
        return self._raw_data

if __name__ == '__main__':
    # Initialize the mocked ECU CANoe
    mocked_ecu_canoe = MockedECUCANoe(id_=1, channel=1, bus='CAN')

    # Power on the ECU CANoe
    print("Powering on the ECU CANoe...")
    mocked_ecu_canoe.power_on_canoe()

    # Read a signal value
    bus = 'CAN'
    channel = 1
    message = 'msg_OperationTime'
    signal = 'Seconds'
    print(f"Reading signal value for {message}, {signal} on {bus} channel {channel}...")
    signal_value = mocked_ecu_canoe.get_signal_value_canoe(bus, channel, message, signal)
    print(f"Signal value: {signal_value}")
    time.sleep(5)
    signal_value = mocked_ecu_canoe.get_signal_value_canoe(bus, channel, message, signal)
    print(f"Signal value: {signal_value}")

    # Power off the ECU CANoe
    print("Powering off the ECU CANoe...")
    mocked_ecu_canoe.power_off_canoe()

    print("Done.")
    # ArgumentParser