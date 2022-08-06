'''Time within a day.'''

from exceptions import TimeError


class TimeOfDay():
    '''Time within a day.'''
    hour: int = 0
    minute: int = 0
    second: int = 0

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        if 0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59:
            self.hour = hour
            self.minute = minute
            self.second = second
        else:
            raise TimeError('Wrong time format.')

    def __repr__(self):
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'
