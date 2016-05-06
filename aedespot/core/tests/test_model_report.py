from datetime import datetime, timedelta, timezone

from django.test import TestCase
from ..models import Report


class ReportModelTest(TestCase):
    def setUp(self):
        self.r = Report.objects.create(
            latitude=-22.5,
            longitude=-43.1,
            type='C'
        )

    def test_report_exists(self):
        '''Report instances should be correctly created.'''
        self.assertTrue(Report.objects.exists())

    def test_report_date(self):
        '''Instances should contain a report date.'''
        self.assertIsInstance(self.r.reported_at, datetime)

    def test_report_date_auto_now(self):
        '''Reported_at should contain current timestamp.'''
        self.assertLess(datetime.now(timezone.utc) + timedelta(seconds=-3), self.r.reported_at)

    def test_geolocation_type(self):
        '''Latitude and longitude should be floats'''
        for field in self.r.latitude, self.r.longitude:
            with self.subTest():
                self.assertIsInstance(field, float)
