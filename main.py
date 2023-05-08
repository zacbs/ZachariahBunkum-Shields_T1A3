import datetime

from alarm import set_alarm
# Prints current time
current_time = datetime.datetime.now(tz=None).strftime('%H:%M')

print(current_time)

alarm_time = input(
    'What time do you want to set the alarm for (Format: 24hr time, 00:00)?')

set_alarm()
