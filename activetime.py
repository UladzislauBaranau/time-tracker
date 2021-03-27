class TimeError(Exception):

    def __str__(self):
        return 'Active session cannot be negative. Check the current time'


class CorrectTimeFormat:

    def __init__(self, time):
        self.hours = time.seconds // 3600
        self.minutes = (time.seconds - self.hours * 3600) // 60
        self.seconds = time.seconds - self.hours * 3600 - self.minutes * 60

    def serialize_time_interval(self):
        if self.hours == 0 and self.minutes == 0:
            return f'{self.seconds} seconds'
        elif self.hours == 0:
            return f'{self.minutes} minutes {self.seconds} seconds'
        return f'{self.hours} hours {self.minutes} minutes {self.seconds} seconds'

    def serialize_total_time(self):
        return f'{self.hours}h {self.minutes}min {self.seconds}sec'

    def serialize_for_json(self):
        return {
            'hours': self.hours,
            'minutes': self.minutes,
            'seconds': self.seconds
        }


class ActiveTime:

    def __init__(self, start, stop):
        self._start = start
        self._stop = stop
        if self._start > self._stop:
            raise TimeError

    def get_diff_time(self):
        return self._stop - self._start

    def get_time_interval(self):
        return CorrectTimeFormat(self.get_diff_time()).serialize_time_interval()
