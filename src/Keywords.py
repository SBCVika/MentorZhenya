from mock_node import MockedECU


class Keywords:
    def __init__(self):
        self._ecu = MockedECU(13, 'CAN0', 100500)
        self._ecus = {13: MockedECU(13, 'CAN0', 100500)}

    def start_ecu(self):
        self._ecu.power_on()

    def stop_ecu(self):
        self._ecu.power_off()

    def read_data_from_ecu(self):
        data = self._ecu.raw_data()
        return [int(ch) for ch in data]

    def ecu_cleanup(self, ecu_id):
        self._ecus[ecu_id].power_off()