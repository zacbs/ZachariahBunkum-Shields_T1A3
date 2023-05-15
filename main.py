import alarm
import filehandler
import menu
from os import system
from pygame import mixer
from threading import Thread
from time import sleep

# Create save file if needed and ensure it is setup correctly
filehandler.file_create()

def main():
    menu.clear_screen()
    print('Welcome to the alarm clock!')
    current_alarms = ', '.join(
        filehandler.active_alarms(filehandler.csv_list()))
    user_input = menu.main_menu(alarm.current_time(), current_alarms)
    while True:
        current_alarms = ', '.join(
            filehandler.active_alarms(filehandler.csv_list()))
        if user_input == '1':
            menu.clear_screen()
            alarm.save_alarm(menu.alarm_menu())
            user_input = '0'
        elif user_input == '2':
            menu.clear_screen()
            user_input2 = menu.saved_menu()
            menu.clear_screen()
            menu.saved_alarm_menu(user_input2)
            user_input = '0'
            user_input = menu.main_menu(alarm.current_time(), current_alarms)
        elif user_input == '3':
            menu.sound_menu()
            user_input = '0'
        elif user_input == '0':
            menu.clear_screen()
            user_input = menu.main_menu(alarm.current_time(), current_alarms)
        else:
            menu.clear_screen()
            print("Invalid input, Try again!")
            user_input = menu.main_menu(alarm.current_time(), current_alarms)


def clock():
    alarm_once = False
    while True:
        sleep(1)
        if alarm.alarm(filehandler.active_alarms(filehandler.csv_list()), alarm.current_time()[-5:]) == True:
            if not alarm_once:
                alarm_once = True
                print('Time to wake up!')
                try:
                    with open('/alarms/activealarm.txt', 'r') as f:
                        alarm_path = f.read()
                    file_path = "/alarms/" + alarm_path
                    mixer.init()
                    alarmsound = mixer.Sound(file_path)
                    alarmsound.play()
                except:
                    print('Error playing sound: No audio device found')


t1 = Thread(target=main)
t2 = Thread(target=clock)

t1.start()
t2.start()
