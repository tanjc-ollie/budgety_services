class SearchInstitutionsRequest:
    def __init__(self,
                 query: str,
                 products: list[str],
                 country_codes: list[str] = ["US","CA"]):
        self.query = query
        self.products = products
        self.country_codes = country_codes