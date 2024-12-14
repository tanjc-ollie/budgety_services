from api.models.plaid.credit import Credit
from api.models.plaid.depository import Depository

class AccountFilters:
    def __init__(self,
                depository: Depository,
                credit: Credit):
        self.depository = depository
        self.credit = credit