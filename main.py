import alarm
import filehandler
import menu
from os import system
# from pygame import mixer
import asyncio

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

menu.clear_screen()
print('Welcome to the alarm clock!')
current_alarms = ', '.join(filehandler.active_alarms(filehandler.csv_list()))
user_input = menu.main_menu(alarm.current_time(), current_alarms)

# TODO: Replace filler with saved alarms
# TODO: Exception handling, breaks if user input not integer
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
  elif user_input == 3:
      print('user pressed 3')
      break
  elif user_input == 0:
      menu.clear_screen()
      user_input = menu.main_menu(alarm.current_time(), current_alarms)
  else:
      menu.clear_screen()
      print("Invalid input, Try again!")
      user_input = menu.main_menu(alarm.current_time(), current_alarms)


# from threading import Thread
# import time

# thread_running = True


# def my_forever_while():
#     global thread_running

#     start_time = time.time()

#     # run this while there is no input
#     while thread_running:
#         time.sleep(0.1)

#         if time.time() - start_time >= 5:
#             start_time = time.time()
#             print('Another 5 seconds has passed')


# def take_input():
#     user_input = input('Type user input: ')
#     # doing something with the input
#     print('The user input is: ', user_input)


# if __name__ == '__main__':
#     t1 = Thread(target=my_forever_while)
#     t2 = Thread(target=take_input)

#     t1.start()
#     t2.start()

#     t2.join()  # interpreter will wait until your process get completed or terminated
#     thread_running = False
#     print('The end')