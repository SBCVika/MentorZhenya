from mock_node import MockedECU
from CANoe_node import MockedECUCANoe

class Keywords:
    def __init__(self):
        self._ecu = MockedECU(13, 'CAN0', 100500)
        self._ecus = {13: MockedECU(13, 'CAN0', 100500)}
        self._ecucanoe = MockedECUCANoe(1, 1,'CAN')

    def start_ecu(self):
        self._ecu.power_on()

    def stop_ecu(self):
        self._ecu.power_off()

    def read_data_from_ecu(self):
        data = self._ecu.raw_data()
        return [int(ch) for ch in data]

    def ecu_cleanup(self, ecu_id):
        self._ecus[ecu_id].power_off()

    def start_ecu_canoe(self):
        self._ecucanoe.power_on_canoe()

    def read_signal_value_from_ecu(self, bus, channel, message, signal, raw_value=True):
        print(
            f"Reading signal value from ECU: bus={bus}, channel={channel}, message={message}, signal={signal}, raw_value={raw_value}")

        try:
            value = self._ecucanoe.get_signal_value_canoe(bus, channel, message, signal, raw_value)
            print(f"Read value: {value}")
            return value
        except Exception as e:
            print(f"Error reading signal value from ECU CANoe: {e}")
            raise
    #    return self._ecucanoe.get_signal_value_canoe(bus, channel, message, signal, raw_value)

    def stop_ecu_canoe(self):
        self._ecucanoe.power_off_canoe()




