import alarm
alarm.file_create()

# TODO: On load need to check if any active alarms exist before continuing

user_input = input('What time would you like to set the alarm for? ')

alarm.save_alarm(user_input)
alarm.alarm(user_input)