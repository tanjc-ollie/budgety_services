from rest_framework import serializers

from api.serializers.institution_serializer import InstitutionSerializer

class SearchInstitutionsResponseSerializer(serializers.Serializer):
    institutions = serializers.ListField(
        child=InstitutionSerializer()
    )