from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APITestCase
from rest_framework import status

from ..models import Robot, Status


class RobotViewTestCase(APITestCase):
    """
    Tests user view operations
    """

    def setUp(self):
        self.robot = mixer.blend('robots.Robot', qa_status=None)

    def test_get_request_returns_robot_list_for_qa(self):
        url = reverse('robot-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_extinguish_updates_a_robot(self):
        robot = mixer.blend(
            'robots.Robot',
            configuration={
                'hasSentience': True,
                'hasWheels': True,
                'hasTracks': True,
                'numberOfRotors': 0,
                'color': '',
            },
            qa_status=None
        )

        on_fire_status, _ = Status.objects.get_or_create(text='on fire')
        robot.status.add(on_fire_status)

        url = f"{reverse('robot-list')}/{robot.id}/extinguish"
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        robot = Robot.objects.get(pk=robot.id)
        self.assertFalse(robot.status.filter(text='on fire'))

    def test_recycle_deletes_a_robot(self):
        robot = mixer.blend(
            'robots.Robot',
            configuration={
                'hasSentience': False,
                'hasWheels': True,
                'hasTracks': True,
                'numberOfRotors': 0,
                'color': '',
            },
            qa_status=None
        )

        url = reverse('robot-list') + '/recycle'

        body = {
            'recycleRobots': [robot.id]
        }

        response = self.client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        with self.assertRaises(Robot.DoesNotExist):
            robot = Robot.objects.get(id=robot.id)
