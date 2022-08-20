'''Bell put in a queue and ready.'''

from datetime import datetime
from typing import TypeVar

QueuedBellSelf = TypeVar("QueuedBellSelf", bound="QueuedBell")


class QueuedBell():
    '''Bell put in a queue and ready.'''
    moment: datetime
    title: str
    sound: str

    def __init__(self, moment, title='', sound=''):
        self.moment = moment
        self.title = title
        self.sound = sound
    
    def __lt__(self, another: QueuedBellSelf) -> bool:
        return self.moment < another.moment
