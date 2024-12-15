from rest_framework import serializers

class CreateTokenResponseSerializer(serializers.Serializer):
    expiration = serializers.CharField(max_length=255)
    link_token = serializers.CharField(max_length=255)
    request_id = serializers.CharField(max_length=255)