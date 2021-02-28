from header import active_foreground  # for Windows
from activity import Activity, ActivitiesStorage
from activetime import ActiveTime
from datetime import datetime
import time


def main():
    active_window = ''
    start_time = datetime.now()
    activities = ActivitiesStorage()

    while True:
        new_window = active_foreground()
        if active_window != new_window:
            stop_time = datetime.now()
            active_time = ActiveTime(start_time, stop_time)
            time_interval = active_time.get_diff_time()
            activity = Activity(active_window, start_time, stop_time)

            if active_window:
                if activity.title not in activities.storage:
                    activities.add_activity(activity)
                else:
                    activities.update_activity(activity)
                print(f'{active_window} - {active_time.get_time_interval(time_interval)}.')
                print(activities.all_activities)
                print()

            active_window = new_window
            start_time = datetime.now()
            time.sleep(1)


main()
