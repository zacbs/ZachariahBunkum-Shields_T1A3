import alarm
import filehandler
from pygame import mixer

filehandler.file_create()

# TODO: Remove playsound it is not working
# TODO: On load need to check if any active alarms exist before continuing

# user_input = input('What time would you like to set the alarm for? ')

# alarm.save_alarm(user_input)
# alarm.alarm(user_input)

mixer.init()

alarmsound = mixer.Sound('/alarms/alarm_1.wav')

print(alarmsound.play())