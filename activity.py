from activetime import ActiveTime, CorrectTimeFormat
from datetime import datetime


class Activity:

    def __init__(self, tab, start, stop):
        self.tab = tab
        self.time_interval = ActiveTime(start, stop).get_diff_time()

    def active_time(self):
        return CorrectTimeFormat(self.time_interval).serialize_for_json()

    def get_activity(self):
        return {
            'active_tab': self.tab,
            'active_sessions': [self.active_time()],
            'last_active_session': self.active_time(),
            'total_time': self.time_interval
        }


class ActivitiesStorage:

    def __init__(self):
        self.storage = []

    def add_activity(self, activity: Activity):
        self.storage.append(activity.get_activity())

    def update_activity(self, activity, time_activity: Activity):
        activity['active_sessions'].append(time_activity.active_time())
        activity['last_active_session'] = time_activity.active_time()
        activity['total_time'] += time_activity.time_interval

    def get_current_activities(self):
        activities = []
        for activity in self.storage:
            tmp_dict = {}
            for key, value in activity.items():
                if key == 'active_tab' or key == 'active_sessions':
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
                if key == 'active_tab' or key == 'last_active_session':
                    tmp_dict[key] = value
                if key == 'total_time':
                    tmp_dict[key] = CorrectTimeFormat(value).serialize_total_time()
            activities.append(tmp_dict)
        return activities

    @property
    def write_to_json_activities_info(self):
        return {
            f'START TIME {datetime.now().strftime("%Y.%m.%d %H:%M")}': self.get_activities_info()
        }
