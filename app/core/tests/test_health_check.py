"""
Test for the health check API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class HealthCheckTest(TestCase):
    """Test the Health Check API."""
    def test_health_check(self):
        """Test health check API."""
        client = APIClient()
        url = reverse('health-check')
        res = client.get(url)
        self.assertEquals(res.status_code, status.HTTP_200_OK)
