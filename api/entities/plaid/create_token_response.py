class CreateTokenResponse:
    def __init__(self,
                 expiration: str,
                 link_token: str,
                 request_id: str):
        self.expiration = expiration
        self.link_token = link_token
        self.request_id = request_id