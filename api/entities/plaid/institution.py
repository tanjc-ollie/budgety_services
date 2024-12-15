class Institution:
    def __init__(self,
                 institution_id: str,
                 name: str,
                 country_codes: list[str] = ["US","CA"]):
        self.institution_id = institution_id
        self.name = name
        self.country_codes = country_codes