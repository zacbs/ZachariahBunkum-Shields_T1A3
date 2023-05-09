import datetime
import time
from os import system


def alarm(alarm_set_point):
    while True:
        # Halts program to only loop once per second
        time.sleep(1)
        current_time = datetime.datetime.now()
        string_time = current_time.strftime('%a, %H:%M')
        system('cls')
        system('clear')
        print('Current time: ' + string_time)
        alarm_set_time = str(current_time.strftime(
            '%a') + ', ' + alarm_set_point)
        print('Alarm time: ' + alarm_set_time)
        if string_time == alarm_set_time:
            print('Wake up!')
            break
