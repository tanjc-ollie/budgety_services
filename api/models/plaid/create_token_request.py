from api.models.plaid.account_filters import AccountFilters
from api.models.plaid.user import User

class CreateTokenRequest:
    def __init__(
                self,
                client_name: str,
                user: User,
                account_filters: AccountFilters,
                products: list[str],
                language: str = "en",
                country_codes: list[str] = ["US","CA"]
                ):
        self.client_name = client_name
        self.user = user
        self.account_filters = account_filters
        self.products = products
        self.language = language
        self.country_codes = country_codes