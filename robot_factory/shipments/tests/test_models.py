from django.test import TestCase
from mixer.backend.django import mixer


class ShipmentModelTestCase(TestCase):
    """
    Defines the test suites to run against the Shipment model.
    """

    def test_model_can_create_shipment(self):
        shipment = mixer.blend('shipments.Shipment')
        self.assertTrue(shipment is not None)
