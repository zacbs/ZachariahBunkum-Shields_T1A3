import alarm
alarm.file_create()
user_input = input('What time would you like to set the alarm for? ')

alarm.save_alarm(user_input)
alarm.alarm(user_input)