import datetime
import nav
# Prints current time
# current_time = datetime.datetime.today()
# print(current_time)


# Ask user if they want to 1. set an alarm, 2. view current saved alarms, 3. add new alarm sounds.
# 1. If user wants to set an alarm, ask what time they want it for
# 2. If user wants to view current saved alarms, show a list of the current saved alarms allow user to select one
# If user wants to edit a saved alarm show settings for that alarm:
# (features on this screen: toggle alarm, allow user to select days to repeat alarm)
# 3. Explain how to add a new sound file ? (flesh this out more)


menu = input('Welcome to the alarm clock! What do you want to do ? \n 1. Set an alarm \n 2. View current saved alarms \n 3. Change alarm sound settings \n')

nav.nav(menu)
