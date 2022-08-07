'''Time within a day.'''

from exceptions import TimeError


class TimeOfDay():
    '''Time within a day.'''
    hour: int
    minute: int

    def __init__(self, hour: int = 0, minute: int = 0):
        if 0 <= hour <= 23 and 0 <= minute <= 59:
            self.hour = hour
            self.minute = minute
        else:
            raise TimeError('Wrong time format.')

    def __repr__(self):
        return f'{self.hour:02}:{self.minute:02}'

    def json_repr(self):
        return {'hour': self.hour, 'minute': self.minute}
