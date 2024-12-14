import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response as HttpResponse
import os

from api.enums.account_types import AccountTypes
from api.models.plaid.account_filters import AccountFilters
from api.models.plaid.create_token_request import CreateTokenRequest
from api.models.plaid.credit import Credit
from api.models.plaid.depository import Depository
from api.models.plaid.user import User
from api.serializers.create_token_request_serializer import CreateTokenRequestSerializer

@api_view(["GET"])
def test(request):
    return HttpResponse({"result": "test endpoint is working"})

@api_view(["GET"])
def get_bank_records(request):
    return HttpResponse()

@api_view(["POST"])
def get_plaid_token(request):
    url: str = "https://sandbox.plaid.com/link/token/create"
    headers = {
        "PLAID-CLIENT-ID": os.getenv("PLAID_CLIENT_ID"),
        "PLAID-SECRET": os.getenv("PLAID_SECRET"),
    }
    user: User = User(client_user_id="placeholder_client_id", legal_name="ollie_tan")
    account_filters: AccountFilters = AccountFilters(
        depository=Depository(account_subtypes=[AccountTypes.CHECKING.value]),
        credit=Credit(account_subtypes=[AccountTypes.CC.value])
    )
    create_token_request: CreateTokenRequest = CreateTokenRequest(
        client_name="budgety_dev", user=user, account_filters=account_filters, products=["transactions"]
    )
    request_serializer = CreateTokenRequestSerializer(create_token_request)

    try:
        response = requests.post(
            url=url,
            headers=headers,
            json=request_serializer.data)
        if response:
            return HttpResponse(response.json())
        else:
            return HttpResponse(response)
        
    except Exception as ex:
        print(ex)
        return HttpResponse(ex)