from django.contrib.auth.models import User 

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Report


class ReportApiTest(APITestCase):
    def setUp(self):
        User.objects.create_superuser('paulo', 'paulo.pinda@gmail.com', '@abc123@')
        data = {'type': 'C', 'latitude': 22.4, 'longitude': 25.5}

        self.client.login(username='paulo', password='@abc123@')
        self.response = self.client.post('/api/v1/reports/', data, format='json')

        self.report = Report.objects.get(pk=1)

    def test_create(self):
        self.assertTrue(Report.objects.exists())

    def test_url(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_type(self):
        self.assertEqual('C', self.report.type)

    def test_latitude(self):
        self.assertEqual(22.4, self.report.latitude)

    def test_longitude(self):
        self.assertEqual(25.5, self.report.longitude)
        

class ReportApiTestLoginInvalid(APITestCase):
    def setUp(self):
        data = {'type': 'C', 'latitude': 22.4, 'longitude': 25.5}

        self.client.login(username='paulo', password='@abc123@')
        self.response = self.client.post('/api/v1/reports/', data, format='json')

        self.report = Report.objects.filter(pk=1)

    def test_create(self):
        self.assertFalse(Report.objects.exists())

    def test_url(self):
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)

