from header import active_foreground
from activetime import ActiveTime
from datetime import datetime
import time


def main():
    active_window = ''
    activities_cache = {}
    start_time = datetime.now()
    while True:
        new_window = active_foreground()
        if active_window != new_window:
            stop_time = datetime.now()
            activity = ActiveTime(start_time, stop_time)
            if active_window not in activities_cache:
                activities_cache[active_window] = activity.get_diff_time()
            else:
                activities_cache[active_window] += activity.get_diff_time()
            if active_window:
                print(f'{active_window} - {activities_cache[active_window]}')
            active_window = new_window
            start_time = datetime.now()
        time.sleep(1)


main()
