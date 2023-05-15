import csv
from filehandler import sample_header
from alarm import current_time
import datetime
# Tests if saved file has corrent headers
def test_csv_first_line():
    with open('saved_alarms.csv', 'r') as file:
        csv_reader = csv.reader(file)
        first_line = next(csv_reader)
    assert first_line == sample_header()
# Tests if current time is accurate is correct
def test_time():
    timetest = datetime.datetime.now()
    timeteststring = timetest.strftime('%a, %H:%M')
    assert current_time() == timeteststring 
