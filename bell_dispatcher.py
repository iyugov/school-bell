'''Dispatcher for bell queue.'''

from schedule_configuration import ScheduleConfiguration
from queue import Queue
from datetime import datetime

class BellDispatcher():
    '''Dispatcher for bell queue.'''
    bell_queue: Queue

    def __init__(self, start_datetime: datetime, schedule_configuration: ScheduleConfiguration):
        self.bell_queue = Queue()
