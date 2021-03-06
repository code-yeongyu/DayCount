#!/usr/local/bin/python3

import json
import datetime
import os

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


json_file = open(os.path.dirname(os.path.realpath(__file__))+'/days.json')
d_days_info = json.load(json_file)['days']

d_days = [Time(d_day) for d_day in d_days_info]

for d_day in d_days:
    date_time_obj = datetime.datetime.strptime(d_day.date, '%Y-%m-%d')
    left_time = date_time_obj - datetime.datetime.now()
    print(f'{d_day.name} | {d_day.date} | ', end="")
    print(f"{bcolors.FAIL}{bcolors.UNDERLINE}{left_time.days} days left.{bcolors.ENDC}")
