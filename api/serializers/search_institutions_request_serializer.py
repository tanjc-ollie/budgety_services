from rest_framework import serializers

class SearchInstitutionsRequestSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=255)
    products = serializers.ListField(
        child=serializers.CharField(max_length=255),
        allow_empty=False
    )
    country_codes = serializers.ListField(
        child=serializers.CharField(max_length=255),
        allow_empty=False
    )