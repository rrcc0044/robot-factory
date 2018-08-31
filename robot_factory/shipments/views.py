from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CreateShipmentSerializer


@api_view(['POST'])
def create_shipment(request):

    if 'shipRobots' not in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    ids = request.data.get('shipRobots')

    data = {
        'shipRobots': ids,
    }

    serializer = CreateShipmentSerializer(data=data)

    if not serializer.is_valid():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    return Response(status=status.HTTP_201_CREATED)
