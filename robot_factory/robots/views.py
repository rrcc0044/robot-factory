from django.db import transaction
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Robot, Status
from .serializers import RobotSerializer


class RobotView(mixins.ListModelMixin,
                viewsets.GenericViewSet):
    queryset = Robot.objects.filter(qa_status=None)
    serializer_class = RobotSerializer

    @action(methods=['put'], detail=True)
    def extinguish(self, request, pk):
        robot = self.get_object()

        # only extinguish the fire if the robot has sentience
        if not robot.configuration['hasSentience']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        on_fire_status = Status.objects.get(text='on fire')
        robot = self.get_object().status.remove(on_fire_status)

        return Response(status=status.HTTP_200_OK)

    @action(methods=['delete'], detail=False)
    def recycle(self, request):
        if 'recycleRobots' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ids = request.data.get('recycleRobots')

        # verify the robots are recyclable
        robots = self.queryset.filter(pk__in=ids)
        for robot in robots:
            if not robots.is_recyclable:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                self.queryset.filter(pk__in=ids).delete()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False)
    def process(self, request):
        if 'processRobots' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ids = request.data.get('processRobots')

        # identify qa status for each robots
        robots = self.queryset.filter(pk__in=ids)
        for robot in robots:
            # check if the robot still has existing status
            if robot.status.all():
                robot.qa_status = 'factory_seconds'
            else:
                robot.qa_status = 'passed_qa'

            robot.save()

        return Response(status=status.HTTP_200_OK)
