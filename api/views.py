import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response as HttpResponse
import os
import json

from api.enums.account_types import AccountTypes
from api.entities.plaid.account_filters import AccountFilters
from api.entities.plaid.create_token_request import CreateTokenRequest
from api.entities.plaid.credit import Credit
from api.entities.plaid.depository import Depository
from api.entities.plaid.user import User
from api.serializers.create_token_request_serializer import CreateTokenRequestSerializer

@api_view(["GET"])
def test(request):
    return HttpResponse({"result": "test endpoint is working"})

@api_view(["GET"])
def get_plaid_transactions(request):
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
            data = json.loads(response.json())
            return HttpResponse(data["link_token"])
        else:
            return HttpResponse(response.reason)
        
    except Exception as ex:
        return HttpResponse("Exception occurred: " + ex)