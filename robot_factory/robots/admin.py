from django.contrib import admin

from .models import Robot, Status


class StatusAdminInline(admin.TabularInline):
    model = Status.robots.through
    extra = 1


class RobotAdmin(admin.ModelAdmin):
    inlines = [StatusAdminInline]


admin.site.register(Robot, RobotAdmin)
admin.site.register(Status)
