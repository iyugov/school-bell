'''Test environment.'''

from schedule_daily_template import ScheduleDailyTemplate
from schedule_configuration import ScheduleConfiguration
from schedule_configuration_group import ScheduleConfigurationGroup
from lesson import Lesson
from event import Event
from time_of_day import TimeOfDay
from datetime import datetime
from bell_dispatcher import BellDispatcher

# Default schedule for all days
global_daily_template = ScheduleDailyTemplate('Обычный день')
global_daily_template.lessons.append(Lesson('1-й урок', TimeOfDay(8, 30), TimeOfDay(9, 10)))
global_daily_template.lessons.append(Lesson('2-й урок', TimeOfDay(9, 20), TimeOfDay(10, 0)))
global_daily_template.lessons.append(Lesson('3-й урок', TimeOfDay(10, 10), TimeOfDay(10, 50)))
global_daily_template.lessons.append(Lesson('4-й урок', TimeOfDay(11, 5), TimeOfDay(11, 45)))
global_daily_template.lessons.append(Lesson('5-й урок', TimeOfDay(11, 55), TimeOfDay(12, 35)))
global_daily_template.lessons.append(Lesson('6-й урок', TimeOfDay(12, 50), TimeOfDay(13, 30)))
global_daily_template.lessons.append(Lesson('7-й урок', TimeOfDay(13, 40), TimeOfDay(14, 20)))
global_daily_template.lessons.append(Lesson('8-й урок', TimeOfDay(14, 35), TimeOfDay(15, 15)))
global_daily_template.lessons.append(Lesson('9-й урок', TimeOfDay(15, 25), TimeOfDay(16, 5)))
global_daily_template.lessons.append(Lesson('10-й урок', TimeOfDay(16, 10), TimeOfDay(16, 50)))

# Schedule for special days
short_daily_template = ScheduleDailyTemplate('Сокращённый день')
short_daily_template.lessons.append(Lesson('1-й урок', TimeOfDay(8, 30), TimeOfDay(9, 0)))
short_daily_template.lessons.append(Lesson('2-й урок', TimeOfDay(9, 10), TimeOfDay(9, 40)))
short_daily_template.lessons.append(Lesson('3-й урок', TimeOfDay(9, 50), TimeOfDay(10, 20)))
short_daily_template.lessons.append(Lesson('4-й урок', TimeOfDay(10, 30), TimeOfDay(11, 00)))
short_daily_template.lessons.append(Lesson('5-й урок', TimeOfDay(11, 10), TimeOfDay(11, 40)))
short_daily_template.lessons.append(Lesson('6-й урок', TimeOfDay(11, 50), TimeOfDay(12, 20)))
short_daily_template.lessons.append(Lesson('7-й урок', TimeOfDay(12, 30), TimeOfDay(13, 00)))
short_daily_template.events.append(Event('Концерт', TimeOfDay(13, 30)))

# Schedule for weekends (empty)
empty_daily_template = ScheduleDailyTemplate('Неучебный день')

# Create configuration
schedule_configuration = ScheduleConfiguration()
# Global
global_configuration_group = ScheduleConfigurationGroup()
global_configuration_group.daily_template = global_daily_template
schedule_configuration.global_configuration = global_configuration_group
# Weekends
weekends_configuration_group = ScheduleConfigurationGroup()
weekends_configuration_group.daily_template = empty_daily_template
schedule_configuration.weekdays_configuration[6] = weekends_configuration_group
schedule_configuration.weekdays_configuration[7] = weekends_configuration_group
# Special
special_configuration_group = ScheduleConfigurationGroup()
special_configuration_group.daily_template = short_daily_template
schedule_configuration.days_configuration[datetime(2022, 9, 1)] = special_configuration_group

test_dispatcher = BellDispatcher(datetime.now(), schedule_configuration)
while not test_dispatcher.bell_queue.empty():
    bell = test_dispatcher.bell_queue.get()
    print(bell)
