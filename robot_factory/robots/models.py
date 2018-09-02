from django.contrib.postgres.fields import JSONField
from django.db import models


def _default_configuration_fields():
    return {
        'hasSentience': False,
        'hasWheels': False,
        'hasTracks': False,
        'numberOfRotors': 0,
        'color': '',
    }


class Robot(models.Model):
    QA_STATUS = (
        ('factory_seconds', 'Factory Seconds'),
        ('passed_qa', 'Passed QA'),
    )

    name = models.CharField(max_length=255)
    configuration = JSONField(default=_default_configuration_fields)
    qa_status = models.CharField(max_length=20, choices=QA_STATUS, null=True)
    shipment = models.ForeignKey(
        'shipments.Shipment',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    @property
    def is_recyclable(self):
        rotors = self.configuration['numberOfRotors']
        wheels = self.configuration['hasWheels']
        color = self.configuration['color']
        is_sentient = self.configuration['hasSentience']
        tracks = self.configuration['hasTracks']
        status = [obj.text for obj in self.status.all()]

        if rotors:
            if color == 'blue' or (rotors < 3 or rotors > 8):
                return True

        if wheels:
            if tracks or 'rusty' in status:
                return True

        if (is_sentient and 'loose screws' in status) or \
           'on fire' in status:
            return True

        return False

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        required_configuration = set(_default_configuration_fields())

        if not set(self.configuration).issubset(required_configuration):
            raise ValueError('configuration not allowed')

        if self.qa_status is not None \
           and not any(self.qa_status in code for code in self.QA_STATUS):

            raise ValueError('qa_status not allowed')

        super().save(*args, **kwargs)


class Status(models.Model):
    robots = models.ManyToManyField(Robot, related_name='status', blank=True)
    text = models.CharField(max_length=50)

    def __str__(self):
        return self.text
