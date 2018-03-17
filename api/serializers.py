from rest_framework import serializers


class TroubleSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=5)
    title = serializers.CharField(max_length=200)
    original_title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    system = serializers.CharField(max_length=100)
    symptoms = serializers.ListField(child=serializers.CharField())
    causes = serializers.ListField(child=serializers.CharField())
    solutions = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        return {
            'code': instance.code,
            'title': instance.title,
            'original_title': instance.original_title,
            'description': instance.description,
            'system': instance.get_system_name(),
            'symptoms': instance.list_symptoms(),
            'causes': instance.list_causes(),
            'solutions': instance.list_solutions(),
        }
