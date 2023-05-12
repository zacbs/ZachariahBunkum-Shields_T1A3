import csv


def csv_list():
    with open('saved_alarms.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    return rows


def sample_header():
    sample_header = ['alarm_time', 'alarm_on', 'Monday', 'Tuesday',
                     'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
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
