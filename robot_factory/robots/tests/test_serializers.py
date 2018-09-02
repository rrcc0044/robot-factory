from django.test import TestCase
from mixer.backend.django import mixer

from ..serializers import RobotSerializer


class RobotSerializerTestCase(TestCase):
    """
    Defines the test suite to be run against the RobotSerializer
    """

    def setUp(self):
        self.robot = mixer.blend('robots.Robot')
        self.serializer = RobotSerializer(instance=self.robot)

    def test_serializer_represent_object_properly(self):
        expected = {
            'id': self.robot.id,
            'name': self.robot.name,
            'configuration': self.robot.configuration,
            'status': [status.text for status in self.robot.status.all()],
            'qa_status': self.robot.qa_status,
        }

        self.assertEqual(self.serializer.data, expected)
