'''Specific lesson.'''

from time_of_day import TimeOfDay


class Lesson():
    '''Specific lesson.'''
    start_time: TimeOfDay
    end_time: TimeOfDay

    def __init__(self, start_time: TimeOfDay, end_time: TimeOfDay):
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return self.start_time
