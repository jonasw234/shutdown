# shutdown_in
Simple Python script to shutdown the computer in the future

Check the releases for a compiled version that doesn’t need a Python installation.

Wrapper around the Windows shutdown command.

Usage:
```
shutdown_in.py 10h30m20s  
shutdown_in.py 25m  
shutdown_in.py 300s  
shutdown_in.py 20
shutdown_in.py 2h-30m
```
I often have a show running in the background and go to bed. This script helps me shutdown my computer after it is done without me having to calculate the time in seconds by hand which is the only unit the default Windows shutdown command recognizes.

You can either run it with the amount of hours, minutes and seconds until shutdown or optionally also add a delta. For example if you’re watching a movie and already watched half an hour, just run with the length of the movie minus the current playtime.

Uses PowerShell to hide the prompt warning you about the imminent shutdown (because it warns you ten minutes before and is quite obtrusive).

## Related
Use [shutdown_at](https://github.com/jonasw234/shutdown_at) to shutdown your computer at a specified time, and [shutdown_a](https://github.com/jonasw234/shutdown_a) to abort a planned shutdown.
