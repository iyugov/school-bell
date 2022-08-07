'''Lesson or another period with start and end times.'''

from time_of_day import TimeOfDay


class Lesson():
    '''Lesson or another period with start and end times.'''
    title: str
    start_time: TimeOfDay
    end_time: TimeOfDay

    def __init__(self, title: str, start_time: TimeOfDay, end_time: TimeOfDay):
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f'{self.title}: {self.start_time}-{self.end_time}'

    def json_repr(self):
        return {
                'title': self.title,
                'start_time': self.start_time.json_repr(),
                'end_time': self.end_time.json_repr()
               }
