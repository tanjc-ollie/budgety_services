from api.entities.plaid.credit import Credit
from api.entities.plaid.depository import Depository

class AccountFilters:
    def __init__(self,
                depository: Depository,
                credit: Credit):
        self.depository = depository
        self.credit = credit