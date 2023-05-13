import csv
import alarm
from os import system

def saved_menu():
    print('Current saved alarms:')
    with open('saved_alarms.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for number, row in enumerate(rows):
            alarm_state = ''
            string_convert = row['alarm_on'] == 'True'
            if string_convert == True:
                alarm_state = 'ON'
            else:
                alarm_state = 'OFF'
            print(
                f'{number + 1}: {row["alarm_time"]}, alarm is currently {alarm_state}')
    print('Press corresponding key to edit that alarm.\nPress q to go back to the main menu.')
    return input()


def saved_alarm_menu(alarm_time):
    print(
        f'Currently editing {alarm_time} alarm.\nPress 1 to turn this alarm on.\nPress 2 to turn on reoccuring alarm.\nPress 3 to delete the current alarm.')
    return int(input())

def main_menu(current_time, active_alarms):
    print(f'The current time is {current_time}.\nYou have alarms set for {active_alarms}\nPress 1 to set a new alarm.\nPress 2 to edit current saved alarms\nPress 3 to edit alarm sounds')
    return int(input())

def alarm_menu():
    user_input = input('What time would you like to set the alarm for?\n')
    print(f'New alarm set for: {user_input}')
    return user_input

def clear_screen():
    system('cls')
    system('clear')