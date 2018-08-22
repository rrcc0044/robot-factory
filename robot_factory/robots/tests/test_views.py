from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .factories import robots


class TestRobotListTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.url = reverse('robot-list')
        self.robots = robots

    def test_get_request_returns_robot_list_for_qa(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
