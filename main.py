from activity import Activity, ActivitiesStorage
from datetime import datetime
from urllib.parse import urlparse
from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_server():
    return 'Hello'


def url_parse(url):
    url = urlparse(url)
    return url.scheme + '://' + url.netloc + '/'


active_tab_url = ''
start_time = datetime.now()
activities = ActivitiesStorage()


@app.route("/", methods=['POST'])
def main():
    global active_tab_url, start_time, activities
    req = request.get_json()
    current_tab_url = req['CurrentURL']
    new_active_tab_url = url_parse(current_tab_url)
    is_first_time_activity = True

    if active_tab_url != new_active_tab_url:
        stop_time = datetime.now()
        current_activity = Activity(active_tab_url, start_time, stop_time)

        if active_tab_url:
            print('Tab has been changed')
            for activity in activities.storage:
                if activity['active_tab'] == current_activity.tab:
                    activities.update_activity(activity, current_activity)
                    is_first_time_activity = False
            if is_first_time_activity:
                activities.add_activity(current_activity)
            with open('activities_info.json', 'w') as file:
                json.dump(activities.write_to_json_current_activities, file, ensure_ascii=False, indent=4)
        active_tab_url = new_active_tab_url
        start_time = datetime.now()

    return req


if __name__ == '__main__':
    app.run()  # app run on the local server 'http://localhost:5000/'
    with open('activities_info.json', 'w') as file:
        json.dump(activities.write_to_json_activities_info, file, ensure_ascii=False, indent=4)
