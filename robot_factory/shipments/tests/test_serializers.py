from django.test import TestCase
from mixer.backend.django import mixer

from ..serializers import CreateShipmentSerializer


class ShipmentSerializerTestCase(TestCase):
    """
    Defines the test suites to be run against the ShipmentSerializer
    """

    def setup(self):
        status = (status for status in ('factory_seconds', 'passed_qa'))
        self.robots = mixer.cycle(10).blend('robots.Robot', qa_status=status)

    def test_serializer_can_save_shipment(self):
        data = {
            'shipRobots': [robot.id for robot in self.robots]
        }

        serializer = CreateShipmentSerializer(data=data)

        self.assertTrue(serializer.is_valid())

        serializer.save()

        # check if the robot shipment id is updated
        for robot in self.robots:
            self.assertEqual(robot.shipment_id, serializer.data.get('id'))

    def test_serializer_can_validate_object(self):
        invalid_robot = mixer.blend('robots.Robot', qa_status=None)

        data = {
            'shipRobots': [invalid_robot.id]
        }

        serializer = CreateShipmentSerializer(data=data)

        self.assertFalse(serializer.is_valid())
