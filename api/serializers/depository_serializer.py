from rest_framework import serializers

class DepositorySerializer(serializers.Serializer):
    account_subtypes = serializers.ListField(
        child = serializers.CharField(max_length = 128),
        allow_empty = True
    )