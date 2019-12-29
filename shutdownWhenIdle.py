import time
import psutil
import os
import sys


def gb_convert(value):
    return value/1024/1024/1024*8

def stats(value):
    print(f"{(gb_convert(value)*100):0.3f} MB/s")

old_value = 0    
seconds_idle = 0

while True:
    new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    diff = new_value - old_value

    if old_value:
        stats(diff)

    if gb_convert(diff) < 0.001:
        seconds_idle+=1
        print(f"seconds idle: ",seconds_idle)
    else:
        seconds_idle = 0

        
    if seconds_idle > 30:
        seconds_idle = 0
        print(f"THIS COMPUTER WILL SHUTDOWN IN 30 SECONDS!")
        os.system("shutdown.exe /s /t 30")
        sys.exit()


    old_value = new_value

    time.sleep(1)