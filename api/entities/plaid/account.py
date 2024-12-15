from abc import ABC

class Account(ABC):
    def __init__(self, account_subtypes: list[str]):
        self.account_subtypes = account_subtypes