'''Schedule within a day.'''

from lesson import Lesson
from time_of_day import TimeOfDay
from json import dump


class DailySchedule():
    '''Schedule within a day.'''
    lessons: list[Lesson] = []
    events: list[TimeOfDay] = []
