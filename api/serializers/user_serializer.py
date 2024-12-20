from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    client_user_id = serializers.CharField(max_length=255)
    legal_name = serializers.CharField(max_length=255)