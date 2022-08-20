'''Schedule template within a day.'''

from lesson import Lesson
from event import Event
from time_of_day import TimeOfDay
from json import dumps


class ScheduleDailyTemplate():
    '''Schedule template within a day.'''
    title: str
    lessons: list[Lesson]
    events: list[Event]

    def __init__(self, title: str = ''):
        self.title = title
        self.lessons = []
        self.events = []

    def json_repr(self) -> str:
        '''Get JSON representation.'''
        template_repr = {'title': self.title}
        template_repr['lessons'] = []
        for lesson in self.lessons:
            template_repr['lessons'].append(lesson.json_repr())
        template_repr['events'] = []
        for event in self.events:
            template_repr['events'].append(event.json_repr())
        return template_repr
