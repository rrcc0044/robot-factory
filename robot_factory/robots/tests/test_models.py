from django.test import TestCase

from robot_factory.robots.models import Robot

from .factories import robots


def RobotModelTestCase(TestCase):
    """
    Defines the test suites to run against the Robot model.
    """

    def setUp(self):
        self.robot = Robot()
    
    def test_model_can_create_a_robot(self):
        robot = Robot()
        old_count = Robot.objects.count()
        robot.save()
        new_count = Robot.objects.count()

        self.assertNotEqual(old_count, new_count)

    def test_model_cant_update_with_illegal_value(self):
        self.fail("TODO Test incomplete")
