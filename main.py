from activetitle import get_active_foreground_title  # for Linux
from activetime import ActiveTime
from activity import Activity, ActivitiesStorage
from datetime import datetime
import time
import json


def main():
    active_title = ''
    start_time = datetime.now()
    activities = ActivitiesStorage()

    while True:
        new_active_title = get_active_foreground_title()
        is_first_time_activity = True

        if active_title != new_active_title:
            stop_time = datetime.now()
            active_time = ActiveTime(start_time, stop_time)
            current_activity = Activity(active_title, start_time, stop_time)

            if active_title:
                print(f"title: {active_title.decode('utf-8')} \n"
                      f"active time: {active_time.get_time_interval()}")
                print()

                for activity in activities.storage:
                    if activity['title'] == current_activity.title:
                        activities.update_activity(activity, current_activity)
                        is_first_time_activity = False

                if is_first_time_activity:
                    activities.add_activity(current_activity)

                with open('current_activities.json', 'w') as file:
                    json.dump(activities.write_to_json_current_activities, file, ensure_ascii=False, indent=4)

            active_title = new_active_title
            start_time = datetime.now()
        time.sleep(1)


main()
