from django.contrib.auth.models import User 

from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Report


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

