'''Dispatcher for bell queue.'''

from schedule_configuration import ScheduleConfiguration
from queue import Queue

class BellDispatcher():
    '''Dispatcher for bell queue.'''
    bell_queue: Queue

    def __init__(self, schedule_configuration: ScheduleConfiguration):
        bell_queue = Queue()
