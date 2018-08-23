from mixer.backend.django import mixer

from django.test import TestCase

from ..serializers import RobotSerializer


class RobotSerializerTestCase(TestCase):

    def setUp(self):
        self.robot = mixer.blend('robots.Robot')
        self.serializer = RobotSerializer(instance=self.robot)
    
    def test_serializer_represent_object_properly(self):
        expected = {
            'id': self.robot.id,
            'configuration': self.robot.configuration,
            'status': [status.text for status in self.robot.status.all()],
        }

        self.assertEqual(self.serializer.data, expected)
