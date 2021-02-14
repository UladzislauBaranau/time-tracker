from header import active_foreground
from activetime import ActiveTime
from datetime import datetime
import time

current_window = ""
all_active_windows = []
spent_time = []
start = datetime.now()


def main():
    global current_window, start
    new_window = active_foreground()

    if current_window != new_window:
        stop = datetime.now()
        activity = ActiveTime(start, stop)

        if current_window not in all_active_windows:
            all_active_windows.append(current_window)
            spent_time.append(activity.get_diff_time())
        else:
            spent_time[all_active_windows.index(current_window)] += activity.get_diff_time()

        index_current_windows = all_active_windows.index(current_window)
        if activity.time_format(spent_time[index_current_windows]) != '0 seconds':
            print(f'Previous window: {current_window} - \
{activity.time_format(spent_time[index_current_windows])}.')

        current_window = new_window
        start = datetime.now()

        print(f'Current window: {current_window}.')
        print()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
