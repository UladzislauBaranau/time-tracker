from activity import Activity, ActivitiesStorage
from activetime import ActiveTime, TimeError
from datetime import datetime
from urllib.parse import urlparse
from flask import Flask, request, jsonify
from flask_cors import CORS
import json


def url_parse(url):
    url = urlparse(url)
    return url.scheme + '://' + url.netloc + '/'


active_tab_url = ''
start_time = datetime.now()
activities = ActivitiesStorage()

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_server():
    return 'Hello'


@app.route("/request", methods=['POST'])
def main():
    global active_tab_url, start_time, activities
    req = request.get_json()
    current_tab_url = req['currentURL']
    new_active_tab_url = url_parse(current_tab_url)
    is_first_time_activity = True

    if active_tab_url != new_active_tab_url:
        try:
            stop_time = datetime.now()
            active_time = ActiveTime(start_time, stop_time)
            current_activity = Activity(active_tab_url, start_time, stop_time)

            if active_tab_url:
                print(
                    '\nWebsite has been changed\n'
                    f'Previous website: {active_tab_url}\n'
                    f'Active time: {active_time.get_time_interval()}'
                )
                for activity in activities.storage:
                    if activity['active_tab'] == current_activity.tab:
                        activities.update_activity(activity, current_activity)
                        is_first_time_activity = False
                if is_first_time_activity:
                    activities.add_activity(current_activity)
                with open('activities_info.json', 'w') as file:
                    json.dump(activities.write_to_json_current_activities, file, ensure_ascii=False, indent=4)
            print(f'\nCurrent website: {new_active_tab_url}\n')

        except TimeError as err:
            print(err)

        finally:
            start_time = datetime.now()
            active_tab_url = new_active_tab_url

    return jsonify(req)


if __name__ == '__main__':
    app.run()  # app run on the local server 'http://localhost:5000/'
    with open('activities_info.json', 'w') as file:
        json.dump(activities.write_to_json_activities_info, file, ensure_ascii=False, indent=4)
