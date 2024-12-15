from api.entities.plaid.institution import Institution

class SearchInstitutionsResponse:
    def __init__(self,
                 institutions: list[Institution]):
        self.institutions = institutions