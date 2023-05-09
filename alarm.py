import datetime
import time
import csv
import os.path
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
        alarm_set_time = str(current_time.strftime('%a') + ', ' + alarm_set_point)
        print('Alarm time: ' + alarm_set_time)
        if string_time == alarm_set_time:
            print('Wake up!')
            break


def save_alarm(alarm_set_point):
    file_exsists = os.path.isfile('saved_alarms.csv')
# This function ensures that the header is only written once and handles if there is no save file present
    if file_exsists:
        with open('saved_alarms.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames[0]

    with open('saved_alarms.csv', 'a', newline='') as f:
        fieldname = ['alarm_time']
        writer = csv.DictWriter(f, fieldnames=fieldname)
        # Write header if file doesn't exist or if no header
        if (file_exsists == False or header != 'alarm_time'):
            writer.writeheader()
        alarmlist = [{'alarm_time': alarm_set_point}]
        writer.writerows(alarmlist)