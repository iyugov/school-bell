'''Schedule configuration.'''

from datetime import datetime
from schedule_specific_configuration import ScheduleSpecificConfiguration


class ScheduleConfiguration():
    '''Schedule configuration.'''
    global_configuration: ScheduleSpecificConfiguration
    weekdays_configuration: list[ScheduleSpecificConfiguration]
    days_configuration: dict[datetime, ScheduleSpecificConfiguration]
    
