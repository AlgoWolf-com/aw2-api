import json
from user_api.function import handler


def test_auth_ept() -> None:
    result = handler(None, None)
    assert result == "Hello World"
