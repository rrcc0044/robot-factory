from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase


class ShipmentViewTestCase(APITestCase):

    def setUp(self):
        self.robots = mixer.cycle(10).blend(
            'robots.Robot',
            qa_status='passed_qa'
        )

    def test_post_creates_shipment(self):
        url = reverse('shipment-create')

        body = {
            'shipRobots': [robot.id for robot in self.robots]
        }

        response = self.client.post(url, body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
