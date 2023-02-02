'''Dispatcher for bell queue.'''

from schedule_configuration import ScheduleConfiguration
from datetime import datetime, timedelta
from queued_bell import QueuedBell
from time import sleep
from pygame import mixer

def start_of_day(date):
    return datetime(date.year, date.month, date.day)

def start_of_second(date):
    return datetime(date.year, date.month, date.day, date.hour, date.minute, date.second)


MIN_QUEUE_LENGTH = 40
SOUND_FILES_PREFIX = 'sounds/'

class BellDispatcher():
    '''Dispatcher for bell queue.'''
    bell_queue: list[QueuedBell]
    start_datetime: datetime
    end_datetime: datetime
    schedule_configuration: ScheduleConfiguration

    def __init__(self, schedule_configuration: ScheduleConfiguration, start_datetime: datetime):
        self.bell_queue = []
        self.schedule_configuration = schedule_configuration
        self.start_datetime = start_datetime
        self.end_datetime = start_datetime
        mixer.init()

    def extend_queue(self, days: int):
        '''Extend queue with given number of days.'''
        start_datetime_extension = self.end_datetime
        end_datetime_extension = self.end_datetime + timedelta(days=days)
        start_span_day = start_of_day(start_datetime_extension)
        end_span_day = start_of_day(end_datetime_extension)
        current_day = start_span_day
        for _ in range(days + 1):
            day_bells = []
            if current_day in self.schedule_configuration.days_configuration:
                current_group = self.schedule_configuration.days_configuration[current_day]
            elif (weekday := current_day.weekday()) in self.schedule_configuration.weekdays_configuration:
                current_group = self.schedule_configuration.weekdays_configuration[weekday]
            else:
                current_group = self.schedule_configuration.global_configuration
            current_sound_set = current_group.sound_file_names
            current_template = current_group.daily_template
            for event in current_template.events:
                moment = event.time.get_moment(current_day)
                if start_datetime_extension <= moment < end_datetime_extension:
                    day_bells.append(QueuedBell(moment, event.title, current_group.sound_file_names['event']))
            for lesson in current_template.lessons:
                moment = lesson.start_time.get_moment(current_day)
                if start_datetime_extension <= moment < end_datetime_extension:
                    day_bells.append(QueuedBell(moment, lesson.title + ' (начало)', current_group.sound_file_names['lesson_start']))
                moment = lesson.end_time.get_moment(current_day)
                if start_datetime_extension <= moment < end_datetime_extension:
                    day_bells.append(QueuedBell(moment, lesson.title + ' (окончание)', current_group.sound_file_names['lesson_end']))
            day_bells.sort(key = lambda bell : bell.moment)
            self.bell_queue.extend(day_bells)
            current_day += timedelta(days=1)
        self.end_datetime = end_datetime_extension

    def main_loop(self, gui_app):
        now = datetime.now()
        upcoming_text = ''
        while len(self.bell_queue) > 0 and self.bell_queue[0].moment < now:
            self.start_datetime = self.bell_queue[0].moment + timedelta(microseconds=1)
            del self.bell_queue[0]
        while len(self.bell_queue) < MIN_QUEUE_LENGTH:
            self.extend_queue(1)
        for bell in self.bell_queue[:7]:
            upcoming_text += f'{bell.moment} {bell.title}\n'
        current_bell = self.bell_queue[0]
        now = start_of_second(datetime.now())
        seconds_left = max(0, int((current_bell.moment - now).total_seconds()))
        hours_left, seconds_left = seconds_left // 3600, seconds_left % 3600
        minutes_left, seconds_left = seconds_left // 60, seconds_left % 60
        upcoming_text += f'До следующего звонка - {hours_left:02}:{minutes_left:02}:{seconds_left:02}\n'
        if now >= current_bell.moment:
            mixer.music.load(SOUND_FILES_PREFIX + current_bell.sound)
            del self.bell_queue[0]
            upcoming_text += f'Звонок: {current_bell.title}\n'
            mixer.music.play()
        gui_app.children['upcoming'].config(text=upcoming_text)
        gui_app.after(1000, self.main_loop, gui_app)
