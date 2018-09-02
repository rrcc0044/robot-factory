from random import choice, randint, randrange

from django.core.management.base import BaseCommand
from mixer.backend.django import mixer

from robot_factory.robots.models import Status


class Command(BaseCommand):
    '''
    Create Robots to try and mimic inventory behavior
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            dest='count',
            default=10,
            type=int,
            help='number of robots to be created',
        )

    def handle(self, *args, **options):
        status = [status for status in Status.objects.all()]
        self.robots = mixer.cycle(options['count']).blend(
            'robots.Robot',
            qa_status=mixer.RANDOM,
        )

        # randomize configurations
        for robot in self.robots:
            config = {
                'hasSentience': choice([True, False]),
                'hasWheels': choice([True, False]),
                'hasTracks': choice([True, False]),
                'numberOfRotors': randint(0, 15),
                'color': choice(['red', 'blue', 'yellow']),
            }
            robot.configuration = config
            robot.status.add(status[randrange(len(status))])
            robot.save()
