from mixer.backend.django import mixer

from django.urls import reverse
from rest_framework.views import reverse_action
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Robot


class RobotViewTestCase(APITestCase):
    """
    Tests /users list operations.
    """

    def setUp(self):
        self.robot = mixer.blend('robots.Robot')

    def test_get_request_returns_robot_list_for_qa(self):
        url = reverse('robot-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_extinguish_updates_a_robot(self):
        url = reverse_action('extinguish', args=[str(self.robot.id)])
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        robot = Robot.objects.get(pk=self.robot.id)
        self.assertFalse(robot.status.filter(text='on fire'))

    def test_recycle_deletes_a_robot(self):
        robot = mixer.blend('robots.Robot')
        url = reverse_action('recycle')
        payload = {'recycleRobots': [robot.id]}

        response = self.client.delete(url, data=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with self.assertRaises(Robot.DoesNotExist):
            Robot.objects.get(pk=robot.id)
