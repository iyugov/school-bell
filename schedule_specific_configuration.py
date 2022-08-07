'''Schedule specific configuration.'''


class ScheduleSpecificConfiguration():
    '''Schedule specific configuration.'''
    sound_file_names: dict[str, str]

    def __init__(self):
        self.sound_file_names = {
                                 'event': '',
                                 'lesson_start': '',
                                 'lesson_end': ''}

    def json_repr(self):
        return self.sound_file_names
