from rest_framework.decorators import api_view


@api_view(['POST'])
def create_shipment(request):
    # validate if the robot ids given already passed QA phase
    pass
