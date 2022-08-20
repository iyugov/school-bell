'''Time within a day.'''

from exceptions import TimeError
from datetime import datetime


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

    def __repr__(self) -> str:
        return f'{self.hour:02}:{self.minute:02}'

    def json_repr(self) -> str:
        '''Get JSON representation.'''
        return {'hour': self.hour, 'minute': self.minute}

    def get_moment(self, date: datetime) -> datetime:
        '''Get datetime as own time within given date.'''
        return datetime(date.year, date.month, date.day, self.hour, self.minute, 0)
