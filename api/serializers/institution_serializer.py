from rest_framework import serializers

class InstitutionSerializer(serializers.Serializer):
    institution_id = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    country_codes = serializers.ListField(
        child=serializers.CharField(max_length=255),
        allow_empty=True
    )