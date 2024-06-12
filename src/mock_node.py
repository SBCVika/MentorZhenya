import random
import string
import time
from threading import Thread


class MockedECU:
    def __init__(self, id_, channel, baudrate):
        self._id = id_
        self._channel = channel
        self._baudrate = baudrate
        self._raw_data = []
        self._on = False
        self._t = None

    def _start_data_gen(self):
        self._t = Thread(target=self._gen_raw_data)
        self._t.daemon = True
        self._t.start()

    def power_on(self):
        self._start_data_gen()
        self._on = True

    def power_off(self):
        time.sleep(1)
        self._on = False

    def is_on(self):
        return self._on

    def raw_data(self):
        return self._raw_data

    def _gen_raw_data(self):
        """
        generates raw_data with
        1 byte - id of ECU
        2 byte - length of data
        3..10 - others
        :return: None
        """
        time.sleep(2)
        while self._on:
            data = [random.choice(string.digits + 'abcdef') for _ in range(random.randint(1,9))]
            self._raw_data = [self._id, len(data), *data]
            self._raw_data = bytes(ord(el) if isinstance(el, str) else el for el in self._raw_data)
            time.sleep(0.0001)
