# shutdown_in
Simple Python script to shutdown the computer in the future

Wrapper around the Windows shutdown command.

Usage:
```
shutdown_in.py 10h30m20s  
shutdown_in.py 25m  
shutdown_in.py 300s  
shutdown_in.py 20
```
I often have a show running in the background and go to bed. This script helps me shutdown my computer after it is done without me having to calculate the time in seconds by hand which is the only unit the default Windows shutdown command recognizes.
