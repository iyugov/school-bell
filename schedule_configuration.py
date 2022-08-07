'''Schedule configuration.'''

from datetime import datetime
from schedule_configuration_group import ScheduleConfigurationGroup


class ScheduleConfiguration():
    '''Schedule configuration.'''
    global_configuration: ScheduleConfigurationGroup
    weekdays_configuration: list[ScheduleConfigurationGroup]
    days_configuration: dict[datetime, ScheduleConfigurationGroup]

    def __init__(self):
        self.global_configuration = ScheduleConfigurationGroup()
        self.weekdays_configuration = []
        self.days_configuration = {}
