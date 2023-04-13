from django.contrib import admin
from missions.models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    pass