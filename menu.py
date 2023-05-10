import csv

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
            print(f'{number + 1}: {row["alarm_time"]}, alarm is currently {alarm_state}')
    print('Press corresponding key to edit that alarm')
    print('Press q to go back to the main menu')


