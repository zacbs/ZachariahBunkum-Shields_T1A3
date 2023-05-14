import alarm
import filehandler
import menu
from os import system
# from pygame import mixer
from threading import Thread

# Create save file if needed and ensure it is setup correctly
filehandler.file_create()

# TODO: Lookg at pygame intro, look for way to remove?
# TODO: Remove playsound it is not working
# TODO: Exception handling, no sound device 

# user_input = input('What time would you like to set the alarm for? ')

# alarm.save_alarm(user_input)
# alarm.alarm(user_input)

# mixer.init()

# alarmsound = mixer.Sound('/alarms/alarm_1.wav')

# alarmsound.play()

# TODO: Replace filler with saved alarms
# TODO: Exception handling, breaks if user input not integer
# TODO: Exception handling, user input on menu.saved_menu

def main():
    menu.clear_screen()
    print('Welcome to the alarm clock!')
    current_alarms = ', '.join(filehandler.active_alarms(filehandler.csv_list()))
    user_input = menu.main_menu(alarm.current_time(), current_alarms)
    while True:
        current_alarms = ', '.join(filehandler.active_alarms(filehandler.csv_list()))
        if user_input == 1:
            menu.clear_screen()
            alarm.save_alarm(menu.alarm_menu())
            user_input = 0
        elif user_input == 2:
            menu.clear_screen()
            user_input2 = menu.saved_menu()
            if user_input2 == 'q':
                user_input = 0
            else:
                menu.clear_screen()
                user_input3 = menu.saved_alarm_menu(user_input2)
                if user_input3 == '1':
                    #   FIX?
                    pass
        elif user_input == 3:
            menu.sound_menu()
            user_input = 0
        elif user_input == 0:
            menu.clear_screen()
            user_input = menu.main_menu(alarm.current_time(), current_alarms)
        else:
            menu.clear_screen()
            print("Invalid input, Try again!")
            user_input = menu.main_menu(alarm.current_time(), current_alarms)


t1 = Thread(target= main)
t2 = Thread(target= )

t1.start()
t2.start()