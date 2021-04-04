from unittest import TestCase
from activetime import ActiveTime, TimeError
from datetime import datetime, timedelta


class TimeTests(TestCase):

    def test_correct_active_time(self):
        start = datetime.now()
        stop = start + timedelta(hours=5)
        self.assertTrue(ActiveTime(start, stop))

    def test_incorrect_active_time(self):
        start = datetime.now()
        stop = start - timedelta(hours=2, minutes=45)
        with self.assertRaises(TimeError) as context:
            ActiveTime(start, stop)

        self.assertTrue('\nSomething is wrong with your time. Check the current time\n' in str(context.exception))

    def test_active_time_more_than_five_hours(self):
        start = datetime.now()
        stop = start + timedelta(hours=5, seconds=1)
        with self.assertRaises(TimeError):
            ActiveTime(start, stop)

    def test_start_is_equal_stop(self):
        start = datetime.now()
        stop = start
        with self.assertRaises(TimeError):
            ActiveTime(start, stop)

    def test_get_diff_time(self):
        start = datetime(year=2021, month=12, day=23, hour=5, minute=45, second=34)
        stop = start + timedelta(minutes=5, seconds=45)
        active_time = ActiveTime(start, stop)
        self.assertEqual(active_time.get_diff_time(), (stop - start))

