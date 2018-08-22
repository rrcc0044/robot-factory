from mixer.backend.django import mixer

from django.test import TestCase

from .factories import robot
from ..models import Robot


class RobotModelTestCase(TestCase):
    """
    Defines the test suites to run against the Robot model.
    """

    def setUp(self):
        self.robot = robot
    
    def test_model_can_create_a_robot(self):
        robot = mixer.blend('robot.Robot')
        self.assertTrue(robot.pk is not None)

    def test_model_cant_create_robot_with_invalid_configuration(self):
        self.assertRaises(ValueError, mixer.blend(
            'robot.Robot',
            categories={'hasPlug': True}
        ))

    def test_model_cant_create_robot_with_invalid_qa_status(self):
        robot = mixer.blend('robot.Robot', qa_status='invalid--')

    def test_model_string_returns_robot_name(self):
        self.assertEqual(str(self.robot), self.robot.name)

    def test_model_is_recyclable_property(self):
        robot = mixer.blend(
            'robot.Robot',
            categories={
                'hasSentience': False,
                'hasWheels': True,
                'hasTracks': True,
                'numberOfRotors': 0,
                'color': '',
            }
        )
        
        self.assertTrue(robot.is_recyclable)
