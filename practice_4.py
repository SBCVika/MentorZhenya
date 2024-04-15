import sys
from argparse import ArgumentParser


class DayOfWeek:
    MONTH_MAPPING = [
        31,
        28,
        31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]
    # 365 days, 6 hours, 9 minutes

    def __init__(self, year=None, month=None, day=None):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def leap_year(n):
        return (n % 100 != 0 or n % 400 == 0) and (n % 4 == 0)

    @classmethod
    def get_month_mapping(cls, year):
        cls.MONTH_MAPPING[1] = 28 if cls.leap_year(year) else 29
        return cls.MONTH_MAPPING


if __name__ == '__main__':
    # ENTRYPOINT
    while True:
        a = 0
        # print(a)
        break

    dow = DayOfWeek()
    print(dow.month)
    dow.month = 'gfreg'
    print(dow.month)
    DayOfWeek.MONTH_MAPPING
    print(DayOfWeek.get_month_mapping(2300))


    # d = {                      # O(1)    hash('greg') == 234 % 10  >  4
    #     'hel': 31,             # O(2)    hash('greg1') == 234 % 10  >  4
    #     'grew': 28,
    #     'greg': 31,
    #     'greg1': 30
    # }

    # 365 * (2024 - 1970)

    # use ArgumentParser