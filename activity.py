from activetime import ActiveTime, CorrectTimeFormat
from datetime import datetime


class Activity:

    def __init__(self, title, start, stop):
        self.title = title
        self.time_interval = ActiveTime(start, stop).get_diff_time()

    def active_time(self):
        return CorrectTimeFormat(self.time_interval).serialize_for_json()

    def get_activity(self):
        return {
            'title': self.title.decode('utf-8'),
            'active sessions': [self.active_time()],
            'last session time': self.active_time(),
            'total time': self.time_interval
        }


class ActivitiesStorage:

    def __init__(self):
        self.storage = []

    def add_activity(self, activity: Activity):
        self.storage.append(activity.get_activity())

    def update_activity(self, activity, time_activity: Activity):
        activity['active sessions'].append(time_activity.active_time())
        activity['last active session'] = time_activity.active_time()
        activity['total time'] += time_activity.time_interval

    def get_current_activities(self):
        activities = []
        for activity in self.storage:
            tmp_dict = {}
            for key, value in activity.items():
                if key == 'title' or key == 'active sessions':
                    tmp_dict[key] = value
            activities.append(tmp_dict)
        return activities

    @property
    def write_to_json_current_activities(self):
        return {
            'CURRENT ACTIVITIES': self.get_current_activities()
        }

    def get_activities_info(self):
        activities = []
        for activity in self.storage:
            tmp_dict = {}
            for key, value in activity.items():
                if key == 'title' or key == 'last active session':
                    tmp_dict[key] = value
                if key == 'total time':
                    tmp_dict[key] = CorrectTimeFormat(value).serialize_total_time()
            activities.append(tmp_dict)
        return activities

    @property
    def write_to_json_activities_info(self):
        return {
            f'START TIME {datetime.now().strftime("%Y.%m.%d %H:%M")}': self.get_activities_info()
        }
