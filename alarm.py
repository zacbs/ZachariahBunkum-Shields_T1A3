import datetime
import csv
import filehandler

def current_time():
    current_time = datetime.datetime.now()
    string_time = current_time.strftime('%a, %H:%M')
    return string_time

def alarm(list, target):
    for item in list:
        if item == target:
            return True
    return False


# Saves current set alarm


def save_alarm(alarm_set_point):
    with open('saved_alarms.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=filehandler.sample_header())
        writer.writerow({'alarm_time': alarm_set_point, 'alarm_on': True, 'reoccur': False, })

