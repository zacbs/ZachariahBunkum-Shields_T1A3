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


def alarm():
    rows = filehandler.csv_list()
    list = []
    print(rows)
    for row in rows:
        pass


# Saves current set alarm


def save_alarm(alarm_set_point):
    with open('saved_alarms.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=filehandler.sample_header())
        writer.writerow({'alarm_time': alarm_set_point, 'alarm_on': True, 'reccour': False, })

alarm()