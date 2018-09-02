from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from robot_factory.robots.views import RobotView
from robot_factory.shipments.views import create_shipment

router = DefaultRouter(trailing_slash=False)
router.register('robots', RobotView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/shipments', create_shipment, name='shipment-create'),
]
