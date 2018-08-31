from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from robot_factory.robots.views import RobotView
from robot_factory.shipments.views import create_shipment

router = DefaultRouter(trailing_slash=False)
router.register('robots', RobotView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shipments/create/', create_shipment, name='shipment-create')
]

urlpatterns += router.urls
