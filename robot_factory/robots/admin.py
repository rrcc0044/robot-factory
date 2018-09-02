from django.contrib import admin

from .models import Robot, Status


class RobotAdmin(admin.ModelAdmin):
    pass


admin.site.register(Robot, RobotAdmin)
admin.site.register(Status)
