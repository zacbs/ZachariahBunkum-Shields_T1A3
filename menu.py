import csv
import alarm
from os import system
import filehandler

# Will either output alarm to edit or q to return to the previous menu


def saved_menu():
    print('Current saved alarms:')
    rows = filehandler.csv_list()
    list = []
    for number, row in enumerate(rows):
        list.append(row['alarm_time'])
        alarm_state = ''
        string_convert = row['alarm_on'] == 'True'
        if string_convert == True:
            alarm_state = 'ON'
        else:
            alarm_state = 'OFF'
        print(
            f'{number + 1}: {row["alarm_time"]}, alarm is currently {alarm_state}')
    user_input = input(
        'Press corresponding key to edit that alarm.\nPress q to go back to the main menu.\n')
    try:
        user_input = int(user_input)
    except ValueError:
        user_output = user_input
    user_output = list[user_input - 1]
    return user_output


def saved_alarm_menu(alarm_time):
    rows = filehandler.csv_list()
    for row in rows:
        alarm_state = ''
        string_convert = row['alarm_on'] == 'True'
        if string_convert == True:
            alarm_state = 'ON'
        else:
            alarm_state = 'OFF'
    user_output = input(
        f'Currently editing {alarm_time} alarm.\nAlarm is currently {alarm_state}\nPress 1 to toggle this alarm.\nPress 2 to turn on reoccuring alarm.\nPress 3 to delete the current alarm.\n')
    if user_output == '1':
        for row in rows:
            string_convert = row['alarm_on'] == 'True'
            if string_convert == True:
                filehandler.value_toggle(alarm_time, 'alarm_on', False)
            else:
                filehandler.value_toggle(alarm_time, 'alarm_on', True)
            clear_screen()
            saved_alarm_menu(alarm_time)

    return user_output


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
