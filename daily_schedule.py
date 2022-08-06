'''Schedule within a day.'''

from lessons import Lesson
from time_of_day import TimeOfDay


class DailySchedule():
    '''Schedule within a day.'''
    lessons: list[Lesson]
    events: List[TimeOfDay]
