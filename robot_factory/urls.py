from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from robot_factory.robots.views import RobotView


router = DefaultRouter(trailing_slash=False)
router.register('robots', RobotView)

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
