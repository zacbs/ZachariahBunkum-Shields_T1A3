import datetime
from time import sleep
import csv
from os import system
import filehandler

# TODO: Refactor core alarm logic out of this function into main.py

def current_time():
    current_time = datetime.datetime.now()
    string_time = current_time.strftime('%a, %H:%M')
    return string_time

# First iteration of the alarm function

def set_alarm(alarm_set_point):
    while True:
        # Halts program to only loop once per second
        sleep(1)
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
            filehandler.value_toggle(alarm_set_point, 'alarm_on', False)
            break

# Saves current set alarm

def save_alarm(alarm_set_point):
    with open('saved_alarms.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=filehandler.sample_header())
        writer.writerow({'alarm_time': alarm_set_point, 'alarm_on': True, 'Monday': False, 'Tuesday': False,
                        'Wednesday': False, 'Thursday': False, 'Friday': False, 'Saturday': False, 'Sunday': False, })
