from rest_framework import serializers

from api.serializers.user_serializer import UserSerializer
from api.serializers.account_filters_serializer import AccountFiltersSerializer

class CreateTokenRequestSerializer(serializers.Serializer):
    client_name = serializers.CharField(max_length = 255)
    user = UserSerializer()
    account_filters = AccountFiltersSerializer()
    products = serializers.ListField(child=serializers.CharField(max_length=255))
    language = serializers.CharField(max_length = 2)
    country_codes = serializers.ListField(child = serializers.CharField(max_length=2),allow_empty=True)