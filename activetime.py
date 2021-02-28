class CorrectTimeFormat:

    def __init__(self, time):
        self.hours = time.seconds // 3600
        self.minutes = (time.seconds - self.hours * 3600) // 60
        self.seconds = time.seconds - self.hours * 3600 - self.minutes * 60

    def serialize_total_time(self):
        if self.hours == 0 and self.minutes == 0:
            return f'{self.seconds} seconds'
        elif self.hours == 0:
            return f'{self.minutes} minutes, {self.seconds} seconds'
        return f'{self.hours} hours, {self.minutes} minutes, {self.seconds} seconds'

    def serialize_time_interval(self):
        return f'{self.hours}h {self.minutes}min {self.seconds}sec'


class ActiveTime:

    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def get_diff_time(self):
        return self._stop - self._start

    @staticmethod
    def get_total_time(total_time):
        return CorrectTimeFormat(total_time).serialize_total_time()

    @staticmethod
    def get_time_interval(time_interval):
        return CorrectTimeFormat(time_interval).serialize_time_interval()


