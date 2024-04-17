from argparse import ArgumentParser

class DayOfWeek:
    MONTH_MAPPING = [
        31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    ]

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

    def day_to_date(self, days, current_year):
        current_month = 1
        month_list = self.get_month_mapping(current_year)
        while days > month_list[current_month - 1]:
            if days > month_list[current_month - 1]:
                days -= month_list[current_month - 1]
                current_month += 1
            else:
                pass
        self.day = days
        self.month = current_month
        self.year = current_year

if __name__ == '__main__':
    # Create ArgumentParser object
    input_args = ArgumentParser(description='Usage: practice_4.py 2024 23')

    # Add arguments
    input_args.add_argument('year', type=int, help='year')
    input_args.add_argument('week', type=int, help='week of year')
    week_args = input_args.parse_args()
    days = (week_args.week) * 7
    dow1 = DayOfWeek()
    dow2 = DayOfWeek()
    dow1.day_to_date(days - 6, week_args.year)
    dow2.day_to_date(days, week_args.year)
    print(f"{week_args.week}: {dow1.year} - {dow1.month} - {dow1.day} - {dow2.year} - {dow2.month} - {dow2.day}")



    # d = {                      # O(1)    hash('greg') == 234 % 10  >  4
    #     'hel': 31,             # O(2)    hash('greg1') == 234 % 10  >  4
    #     'grew': 28,
    #     'greg': 31,
    #     'greg1': 30
    # }

    # 365 * (2024 - 1970)

    # use ArgumentParser
    #python weekday.py 2024 23
    #23: 2024-05-10 - 2024-05-17
