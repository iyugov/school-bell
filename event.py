'''Event with one time.'''

from time_of_day import TimeOfDay


class Event():
    '''Event with one time.'''
    title: str
    time: TimeOfDay

    def __init__(self, title: str, time: TimeOfDay):
        self.title = title
        self.time = time

    def __repr__(self):
        return f'{self.title}: {self.time}'

    def json_repr(self):
        return {
                'title': self.title,
                'time': self.time.json_repr()
               }
