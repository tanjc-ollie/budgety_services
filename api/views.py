import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response as HttpResponse
import os

from api.models import LinkToken, Institution

from api.enums.account_types import AccountTypes
from api.entities.plaid.account_filters import AccountFilters
from api.entities.plaid.create_token_request import CreateTokenRequest
from api.entities.plaid.credit import Credit
from api.entities.plaid.depository import Depository
from api.entities.plaid.user import User
from api.serializers.create_token_request_serializer import CreateTokenRequestSerializer
from api.serializers.create_token_response_serializer import CreateTokenResponseSerializer
from api.entities.plaid.search_institutions_request import SearchInstitutionsRequest
from api.serializers.search_institutions_request_serializer import SearchInstitutionsRequestSerializer
from api.serializers.search_institutions_response_serializer import SearchInstitutionsResponseSerializer

@api_view(["GET"])
def test(request):
    return HttpResponse({"result": "test endpoint is working"})

@api_view(["POST"])
def search_plaid_institutions(request):
    url = "https://sandbox.plaid.com/institutions/search"
    search_word: str = "td canada trust"
    headers = {
        "PLAID-CLIENT-ID": os.getenv("PLAID_CLIENT_ID"),
        "PLAID-SECRET": os.getenv("PLAID_SECRET"),
    }
    req = SearchInstitutionsRequest(query=search_word,products=["transactions"],country_codes=["CA"])
    req_ser = SearchInstitutionsRequestSerializer(req)

    try:
        response = requests.post(
            url=url,
            headers=headers,
            json=req_ser.data
        )

        if response:
            data = response.json()
            res_ser = SearchInstitutionsResponseSerializer(data=data)
            if res_ser.is_valid(raise_exception=True):
                valid_data = res_ser.validated_data
                institutions = valid_data["institutions"]
                for i in institutions:
                    Institution.objects.get_or_create(
                        institution_id=i["institution_id"],
                        name=i["name"]
                    )

                return HttpResponse(institutions)
    except Exception as ex:
        return HttpResponse("Exception occurred: " + ex)

@api_view(["POST"])
def get_plaid_link_token(request):
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
            json=request_serializer.data
        )
        if response:
            data = response.json()
            response_serializer = CreateTokenResponseSerializer(data=data)
            if response_serializer.is_valid(raise_exception=True):
                valid_data = response_serializer.validated_data
                token = LinkToken.objects.create(
                    user_id="test_user",
                    token=valid_data["link_token"],
                    expiration=valid_data["expiration"]
                )
                return HttpResponse({"token":token.token})
            else:
                return HttpResponse(response_serializer.error_messages)
        else:
            return HttpResponse(response.reason)
        
    except Exception as ex:
        return HttpResponse("Exception occurred: " + ex)

@api_view(["POST"])
def get_plaid_transactions(request):
    return HttpResponse()