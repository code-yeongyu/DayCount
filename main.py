import json
import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Time:
    def __init__(self, date_object):
        self.name = date_object["name"]
        self.date = date_object["time"]


json_file = open('./days.json')
d_days_info = json.load(json_file)['days']

d_days = [Time(d_day) for d_day in d_days_info]

for d_day in d_days:
    date_time_obj = datetime.datetime.strptime(d_day.date, '%Y-%m-%d %H:%M:%S')
    left_time = datetime.datetime.now() - date_time_obj
    print(f'{d_day.name}: ', end="")
    print(f"{bcolors.FAIL}{bcolors.UNDERLINE}{left_time.days}{bcolors.ENDC}")