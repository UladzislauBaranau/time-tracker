class ActiveTime:

    def __init__(self, start_activity, stop_activity):
        self._start = start_activity
        self._stop = stop_activity
        self._time_diff = stop_activity - start_activity

    def get_diff_time(self):
        return self._time_diff

    def time_format(self, active_time):
        days = active_time.days
        hours = active_time.seconds // 3600
        minutes = (active_time.seconds - hours * 3600) // 60
        seconds = active_time.seconds - hours * 3600 - minutes * 60

        if days == 0 and hours == 0 and minutes == 0:
            return f'{seconds} seconds'
        elif days == 0 and hours == 0:
            return f'{minutes} minutes, {seconds} seconds'
        elif days == 0:
            return f'{hours} hours, {minutes} minutes, {seconds} seconds'
        else:
            return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'


