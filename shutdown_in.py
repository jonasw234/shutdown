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
"""
import re
import os
import sys


def main(argv):
    if len(argv) != 2:
        print('Usage: shutdown_in.py 1h1m1s.')
        return 1
    time_string = re.match('(\d+h)?(\d+m)?(\d+s?)?', argv[1]).groups()
    if time_string is not None:
        seconds = 0
        if time_string[0]: # hours
            seconds += 60*60*int(time_string[0][:-1])
        if time_string[1]: # minutes
            seconds += 60*int(time_string[1][:-1])
        if time_string[2]: # seconds
            try:
                seconds += int(time_string[2])
            except Exception:
                seconds += int(time_string[2][:-1])
        os.system('shutdown -s -f -t ' + str(seconds))
        return 0
    else:
        print('Usage: shutdown_in.py 1h1m1s.')
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv))
