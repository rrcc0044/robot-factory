from django.test import TestCase
from mixer.backend.django import mixer


class RobotModelTestCase(TestCase):
    """
    Defines the test suites to run against the Robot model.
    """

    def test_model_can_create_a_robot(self):
        robot = mixer.blend('robots.Robot')
        self.assertTrue(robot is not None)

    def test_model_cant_create_robot_with_invalid_configuration(self):
        with self.assertRaises(ValueError):
            mixer.blend(
                'robots.Robot',
                configuration={'hasPlug': True}
            )

    def test_model_cant_create_robot_with_invalid_qa_status(self):
        with self.assertRaises(ValueError):
            mixer.blend(
                'robots.Robot', qa_status='invalid--'
            )

    def test_model_string_returns_robot_name(self):
        robot = mixer.blend('robots.Robot')
        self.assertEqual(str(robot), robot.name)

    def test_model_is_recyclable_returns_true_for_recyclable_robots(self):
        robot = mixer.blend(
            'robots.Robot',
            configuration={
                'hasSentience': False,
                'hasWheels': True,
                'hasTracks': True,
                'numberOfRotors': 0,
                'color': '',
            }
        )

        self.assertTrue(robot.is_recyclable)

    def test_model_is_recyclable_returns_false_for_nonrecyclable_robots(self):
        robot = mixer.blend(
            'robots.Robot',
            configuration={
                'hasSentience': False,
                'hasWheels': True,
                'hasTracks': False,
                'numberOfRotors': 0,
                'color': '',
            }
        )

        self.assertFalse(robot.is_recyclable)


class StatusModelTestCase(TestCase):
    """
    Defines the test suites to run against the Status model.
    """

    def setUp(self):
        self.robot = mixer.blend('robots.Robot')

    def test_model_can_create_status(self):
        status = mixer.blend('robots.Status')
        self.assertTrue(status is not None)

    def test_model_can_associate_to_user(self):
        status = mixer.blend('robots.Status')
        self.robot.status.add(status)

        self.assertTrue(len(self.robot.status.filter(text=status.text)) == 1)

    def test_model_string_returns_text(self):
        status = mixer.blend('robots.Status')
        self.assertEqual(str(status), status.text)
