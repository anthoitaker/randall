from django.contrib import admin
from core.models import Cause, Solution, Symptom, System, Trouble


class BaseAdmin(admin.ModelAdmin):
    empty_value_display = 'None'
    list_per_page = 15


@admin.register(System)
class SystemAdmin(BaseAdmin):
    search_fields = ['name']
    list_display = ['name', 'troubles', 'created_at', 'updated_at']

    def troubles(self, obj):
        return Trouble.objects.filter(system=obj).count()


@admin.register(Trouble)
class TroubleAdmin(BaseAdmin):
    search_fields = ['code', 'title', 'system__name']
    list_display = ['code', 'title', 'system', 'symptoms', 'causes', 'solutions', 'created_at', 'updated_at']
    list_select_related = ['system']

    def symptoms(self, obj):
        return Symptom.objects.filter(trouble=obj).count()

    def causes(self, obj):
        return Cause.objects.filter(trouble=obj).count()

    def solutions(self, obj):
        return Solution.objects.filter(trouble=obj).count()


@admin.register(Symptom)
class SymptomAdmin(BaseAdmin):
    search_fields = ['trouble__code', 'description']
    list_display = ['trouble', 'description', 'repetitions', 'created_at', 'updated_at']
    list_select_related = ['trouble']

    def repetitions(self, obj):
        return Symptom.objects.filter(description=obj.description).count()


@admin.register(Cause)
class CauseAdmin(BaseAdmin):
    search_fields = ['trouble__code', 'description']
    list_display = ['trouble', 'description', 'repetitions', 'created_at', 'updated_at']
    list_select_related = ['trouble']

    def repetitions(self, obj):
        return Cause.objects.filter(description=obj.description).count()


@admin.register(Solution)
class SolutionAdmin(BaseAdmin):
    search_fields = ['trouble__code', 'description']
    list_display = ['trouble', 'description', 'repetitions', 'created_at', 'updated_at']
    list_select_related = ['trouble']

    def repetitions(self, obj):
        return Solution.objects.filter(description=obj.description).count()
