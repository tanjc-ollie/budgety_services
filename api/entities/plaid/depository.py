from api.entities.plaid.account import Account

class Depository(Account):
    def __init__(self,
                 account_subtypes: list[str]):
        super().__init__(account_subtypes)