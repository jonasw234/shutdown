#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shutdown in

Wrapper around the Windows shutdown command.
Usage:
    shutdown_in.py 10h30m20s
    shutdown_in.py 25m
    shutdown_in.py 300s
    shutdown_in.py 20 (assumes seconds)
    shutdown_in.py 2h-30m
"""
import re
import os
import sys


def to_int(time_element):
    if time_element:
        try:
            return int(time_element)
        except Exception:
            return int(time_element[:-1])
    return 0


def usage():
    print('Usage: shutdown_in.py 1h1m1s' \
          '       shutdown_in.py 2h-10m')
    return 1


def main(argv):
    if len(argv) != 2:
        return usage()
    __import__('ipdb').set_trace()

    time_string = ''.join(argv[1:])
    time_groups = re.match('(\d+h)?(\d+m)?(\d+s?)?(\s*-\s*(\d+h)?(\d+m)?(\d+s?)?)?',
                           time_string).groups()

    if time_groups is not None:
        seconds = 60*60*to_int(time_groups[0])  # Hours
        seconds += 60*to_int(time_groups[1])  # Minutes
        seconds += to_int(time_groups[2])  # Seconds
        seconds -= 60*60*to_int(time_groups[4])  # Hours
        seconds -= 60*to_int(time_groups[5])  # Minutes
        seconds -= to_int(time_groups[6])  # Seconds
        os.system('powershell.exe -WindowStyle Hidden -Command "sleep {}; shutdown -s -f -t 0"'.format(seconds))
        return 0
    else:
        return usage()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
