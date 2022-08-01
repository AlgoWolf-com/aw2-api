class ApiError(Exception):
    def __init__(self, msg: str, code: int) -> None:
        super().__init__()
        self.msg = msg
        self.code = code
