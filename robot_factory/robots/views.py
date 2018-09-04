from django.db import transaction, IntegrityError
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Robot, Status
from .serializers import RobotSerializer


class RobotView(mixins.ListModelMixin,
                viewsets.GenericViewSet):
    queryset = Robot.objects.filter(shipment=None)
    serializer_class = RobotSerializer
    authentication_classes= set()

    @action(methods=['put'], detail=True)
    def extinguish(self, request, pk):
        robot = self.get_object()

        # only extinguish the fire if the robot has sentience
        if not robot.configuration['hasSentience']:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        on_fire_status = Status.objects.get(text='on fire')
        robot = self.get_object()
        robot.status.remove(on_fire_status)
        serializer = self.serializer_class(robot)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def recycle(self, request):
        if 'recycleRobots' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ids = request.data.get('recycleRobots')

        # verify the robots are recyclable
        robots = self.queryset.filter(pk__in=ids)
        for robot in robots:
            if not robot.is_recyclable:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                robots.delete()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def process(self, request):
        if 'processRobots' not in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        ids = request.data.get('processRobots')

        # identify qa status for each robots
        robots = self.queryset.filter(pk__in=ids)
        try:
            with transaction.atomic():
                for robot in robots:
                    if robot.is_recyclable:
                        raise IntegrityError()

                    # check if the robot still has existing status
                    if robot.status.all():
                        robot.qa_status = 'factory_seconds'
                    else:
                        robot.qa_status = 'passed_qa'

                    robot.save()

        except IntegrityError:
            Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(robots, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
