from os import system
import filehandler
import sys

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
        'Press corresponding key to edit that alarm.\n')
    user_output = int(user_input)
    user_output2 = list[user_output - 1]
    return user_output2


def saved_alarm_menu(alarm_time):
    rows = filehandler.csv_list()
    user_output = input(
        f'Currently editing {alarm_time} alarm.\nPress 1 to toggle this alarm.\nPress 2 to turn on reoccuring alarm.\nPress 3 to delete the current alarm.\n')
    if user_output == '1':
        for row in rows:
            string_convert = row['alarm_on'] == 'True'
            if string_convert == True:
                filehandler.value_toggle(alarm_time, 'alarm_on', False)
            else:
                filehandler.value_toggle(alarm_time, 'alarm_on', True)
            clear_screen()
            return
    elif user_output == '2':
        clear_screen()
        alarm_reoccur = input('Do you want this alarm to reoccur? (y/n)\n')
        if alarm_reoccur == 'y':
            filehandler.value_toggle(alarm_time, 'reoccur', True)
            clear_screen()
        if alarm_reoccur == 'n':
            filehandler.value_toggle(alarm_time, 'reoccur', False)
            clear_screen()
    elif user_output == '3':
        clear_screen()
        filehandler.delete_alarm(alarm_time)
    return


def main_menu(current_time, active_alarms):
    print(f'The current time is {current_time}.\nYou have alarms set for {active_alarms}\nPress 1 to set a new alarm.\nPress 2 to edit current saved alarms\nPress 3 to edit alarm sounds')
    return input()


def alarm_menu():
    user_input = input('What time would you like to set the alarm for?\n')
    print(f'New alarm set for: {user_input}')

    return user_input


def clear_screen():
    system('cls')
    system('clear')


def sound_menu():
    clear_screen()
    with open('alarms/activealarm.txt', 'r') as f:
        print(f'Currently using {f.read()} sound')
    user_input = input('Do you want to change the active sound? (y/n)\n')
    if user_input == 'y':
        clear_screen()
        user_input = input('Please write the file name of the sound you want to use.\nDefault sounds are named alarm_1.wav, alarm_2.wav, alarm_3.wav, alarm_4.wav, alarm_5.wav, alarm_6.wav\nIf you want a custom sound, add the mp3 or wav file to the alarms folder and enter the file name here\n')
        with open('alarms/activealarm.txt', 'w') as f:
            f.write(user_input)
    else:
        return