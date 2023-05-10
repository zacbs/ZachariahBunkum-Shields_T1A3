import datetime
from time import sleep
import csv
from os import system

# Exception handling for file creation and setting up the file for use if it is not correctly setup

sample_header = ['alarm_time', 'alarm_on', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def file_create():
    try:
        with open('saved_alarms.csv', 'x', newline='') as f:
            writer = csv.writer(f)            
            writer.writerow(sample_header)
            pass       
    except FileExistsError:
        with open('saved_alarms.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
        if header != sample_header:
            with open('saved_alarms.csv', 'w', newline='') as f:
                writer = csv.writer(f)            
                writer.writerow(sample_header)

def alarm(alarm_set_point):
    while True:
        # Halts program to only loop once per second
        sleep(1)
        current_time = datetime.datetime.now()
        string_time = current_time.strftime('%a, %H:%M')
        system('cls')
        system('clear')
        print('Current time: ' + string_time)
        alarm_set_time = str(current_time.strftime('%a') + ', ' + alarm_set_point)
        print('Alarm time: ' + alarm_set_time)
        if string_time == alarm_set_time:
            print('Wake up!')
            value_toggle(alarm_set_point, 'alarm_on', False)
            break

# Saves current set alarm
def save_alarm(alarm_set_point):
    with open('saved_alarms.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f,fieldnames=sample_header)
        writer.writerow({'alarm_time':alarm_set_point, 'alarm_on':True, 'Monday':False, 'Tuesday':False, 'Wednesday':False, 'Thursday':False, 'Friday':False, 'Saturday':False, 'Sunday':False,})


def value_toggle(target_row, target_column, target_value):
    rows = []
    with open('saved_alarms.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    for row in rows:
        if row['alarm_time'] == target_row:
            row[target_column] = target_value

    # Write the updated rows back to the CSV file
    with open('saved_alarms.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=sample_header)
        writer.writeheader()
        writer.writerows(rows)