'''Schedule specific configuration.'''

from schedule_daily_template import ScheduleDailyTemplate


class ScheduleSpecificConfiguration():
    '''Schedule specific configuration.'''
    sound_file_names: dict[str, str]
    daily_template: ScheduleDailyTemplate

    def __init__(self):
        self.sound_file_names = {
                                 'event': '',
                                 'lesson_start': '',
                                 'lesson_end': ''}
        self.daily_template = ScheduleDailyTemplate('')

    def json_repr(self):
        return {
                'sounds' : self.sound_file_names,
                'daily_template': self.daily_template.json_repr()
               }
