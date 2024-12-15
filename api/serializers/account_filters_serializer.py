from rest_framework import serializers

from api.serializers.depository_serializer import DepositorySerializer
from api.serializers.credit_serializer import CreditSerializer

class AccountFiltersSerializer(serializers.Serializer):
    depository = DepositorySerializer()
    credit = CreditSerializer()