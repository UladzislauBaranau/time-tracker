from activetime import ActiveTime


class Activity:

    def __init__(self, title, start, stop):
        self.title = title
        self.time_interval = ActiveTime(start, stop).get_diff_time()

    def get_active_time(self):
        return {
            'total time': self.time_interval,
            'last session': self.time_interval
        }

    def get_activity(self):
        return {
            self.title: self.get_active_time()
        }


class ActivitiesStorage:

    def __init__(self):
        self.storage = {}

    def add_activity(self, activity: Activity):
        self.storage[activity.title] = activity.get_active_time()

    def update_activity(self, activity: Activity):
        self.storage[activity.title]['total time'] += activity.time_interval
        self.storage[activity.title]['last session'] = activity.time_interval

    @property
    def all_activities(self):
        return self.storage
