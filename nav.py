def nav(self):
  if self == ('1' or '1.'):
      self = '0'
      alarmtime = input('What time you want the alarm to be set the alarm to?')
  elif self == ('2' or '2.'):
      self = '0'
      print('Saved alarms:')
  elif self == ('3' or '3.'):
      print('This is the settings page for the alarm sounds')
  else:
      print('This is not a valid input!')
      nav()