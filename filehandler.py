import csv

def csv_list():
    with open('saved_alarms.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows

def sample_header():
    sample_header = ['alarm_time', 'alarm_on', 'reoccur']
    return sample_header

def file_create():
    try:
        with open('saved_alarms.csv', 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(sample_header())
            pass
    except FileExistsError:
        with open('saved_alarms.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            header = reader.fieldnames
        if header != sample_header():
            with open('saved_alarms.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(sample_header())

def value_toggle(target_row, target_column, target_value):
    rows = []
    with open('saved_alarms.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    for row in rows:
        if row['alarm_time'] == target_row:
            row[target_column] = target_value
    with open('saved_alarms.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=sample_header())
        writer.writeheader()
        writer.writerows(rows)

def active_alarms(list):
    active_alarm = []
    for dict in list:
        if dict['alarm_on'] == 'True':
            active_alarm.append(dict['alarm_time'])
    return active_alarm

def delete_alarm(alarm_time):
    with open('saved_alarms.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    with open('saved_alarms.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row and row[0] != alarm_time:
                csv_writer.writerow(row)

delete_alarm('19:40')