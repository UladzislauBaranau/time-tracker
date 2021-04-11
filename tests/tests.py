import unittest
from activetime import ActiveTime, TimeError
from activity import Activity, ActivitiesStorage
from datetime import datetime, timedelta


class TimeTests(unittest.TestCase):

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


class ActivityTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.activities = ActivitiesStorage()
        cls.a = Activity('title', datetime.now() - timedelta(hours=1, minutes=15), datetime.now())
        cls.a2 = Activity('title2', datetime.now() - timedelta(minutes=4, seconds=23), datetime.now())

        cls.activities2 = ActivitiesStorage()
        cls.activities2.storage = [
            {
                'active_tab': 'title3',
                'active_sessions': [{'hours': 2, 'minutes': 20, 'seconds': 0}],
                'last_active_session': {'hours': 2, 'minutes': 20, 'seconds': 0},
                'total_time': timedelta(seconds=8400, microseconds=11)
            }
        ]
        cls.a3 = Activity('title3', datetime.now() - timedelta(minutes=12, seconds=45), datetime.now())

    def test_add_activity(self):
        self.activities.add_activity(self.a)
        self.activities.add_activity(self.a2)
        self.assertIn('title', self.activities.storage[0]['active_tab'])
        self.assertIn('title2', self.activities.storage[1]['active_tab'])

    def test_update_activity(self):
        self.activities.update_activity(self.activities2.storage[0], self.a3)
        self.assertEqual(len(self.activities2.storage[0]['active_sessions']), 2)
        self.assertEqual(len(self.activities2.storage), 1)


if __name__ == '__main__':
    unittest.main()
