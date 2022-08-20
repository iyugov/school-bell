'''Bell put in a queue and ready.'''

from datetime import datetime


class QueuedBell():
    '''Bell put in a queue and ready.'''
    moment: datetime
    title: str
    sound: str

    def __init__(self, moment, title='', sound=''):
        self.moment = moment
        self.title = title
        self.sound = sound
