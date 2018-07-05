from django.contrib import admin
from core.models import Cause, Solution, Symptom, System, Trouble


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = 'None'


@admin.register(System)
class SystemAdmin(BaseAdmin):
    search_fields = ['name']
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(Trouble)
class TroubleAdmin(BaseAdmin):
    search_fields = ['code']
    list_display = ['code', 'title', 'system', 'created_at', 'updated_at']


@admin.register(Symptom)
class SymptomAdmin(BaseAdmin):
    search_fields = ['description']
    list_display = ['trouble', 'description', 'created_at', 'updated_at']


@admin.register(Cause)
class CauseAdmin(BaseAdmin):
    search_fields = ['description']
    list_display = ['trouble', 'description', 'created_at', 'updated_at']


@admin.register(Solution)
class SolutionAdmin(BaseAdmin):
    search_fields = ['description']
    list_display = ['trouble', 'description', 'created_at', 'updated_at']
