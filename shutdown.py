#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shutdown

Wrapper around the Windows shutdown command.
Usage:
    shutdown.py 10h30m20s
    shutdown.py 25m
    shutdown.py 300s
    shutdown.py 10:20
    shutdown.py 10:20:30
    shutdown.py 20 (assumes o’clock)
"""
from datetime import datetime
import re
import os
import sys
import time


def main(argv):
    if len(argv) != 2:
        print(argv)
        print('Usage: shutdown.py <1h1m1s|10:20:30>.')
        return 1

    seconds = None
    try:
        shutdown_time = datetime.strptime(argv[1], '%H:%M:%S')
    except ValueError:
        try:
            shutdown_time = datetime.strptime(argv[1], '%H:%M')
        except ValueError:
            try:
                shutdown_time = datetime.strptime(argv[1], '%H')
            except ValueError:
                time_string = ''.join(argv[1:])
                time_groups = re.match(r'(\d+h)?(\d+m)?(\d+s?)?(\s*-\s*(\d+h)?(\d+m)?(\d+s?)?)?', time_string).groups()
                if time_groups is not None:
                    seconds = 0
                    if time_groups[0]: # hours
                        seconds += 60*60*int(time_groups[0][:-1])
                    if time_groups[1]: # minutes
                        seconds += 60*int(time_groups[1][:-1])
                    if time_groups[2]: # seconds
                        seconds += int(time_groups[2].replace('s', ''))
                else:
                    print('Usage: shutdown.py <1h1m1s|10:20:30>.')
                    return 1
    if not seconds:
        now = datetime.now()
        shutdown_time = shutdown_time.replace(year=now.year, month=now.month, day=now.day)
        if shutdown_time < now:
            shutdown_time.replace(day=shutdown_time.day+1)
        seconds = (shutdown_time - now).seconds
    os.system(f'powershell.exe -WindowStyle Hidden -Command "sleep {seconds}; shutdown -s -f -t 0"')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
