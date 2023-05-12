import csv
import alarm

def menu_saved():
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


def menu_saved_alarm(alarm_time):
    print(
        f'Currently editing {alarm_time} alarm.\nPress 1 to turn this alarm on.\nPress 2 to turn on reoccuring alarm.\nPress 3 to delete the current alarm.')
    return input()

def main_menu():
    print('Welcome to the alarm clock!\nThis')
    pass