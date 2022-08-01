# pylint: disable=redefined-outer-name,import-outside-toplevel
import os
import json
from unittest import mock
from typing import Callable, Mapping
import pytest


class MockLambdaContext:
    aws_request_id = "abcd123456"


@pytest.fixture(autouse=True)
def mock_settings_env_vars():
    with mock.patch.dict(
        os.environ,
        {
            "COGNITO_APP_CLIENT_ID": "6ogk3o03rlqivg2jtmslve4eu3",
            "AWS_REGION": "ap-southeast-2",
        },
    ):
        yield


@pytest.fixture
def handler() -> Callable:
    from user_api.function import handler

    return handler


@pytest.fixture
def get_message_event() -> Mapping:
    return {
        "version": "2.0",
        "routeKey": "ANY /users/{proxy+}",
        "rawPath": "/Dev/users/message",
        "rawQueryString": "",
        "headers": {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "content-length": "22",
            "content-type": "application/json",
            "host": "api.ethanhollins.com",
            "postman-token": "59685e20-4201-41ce-9642-7d72a991df07",
            "user-agent": "PostmanRuntime/7.29.2",
            "x-amzn-trace-id": "Root=1-62e77021-1cbaedee03c8e5d57b76cc04",
            "x-forwarded-for": "220.240.78.250",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
        },
        "requestContext": {
            "accountId": "977407872120",
            "apiId": "frd6dnh21f",
            "domainName": "api.ethanhollins.com",
            "domainPrefix": "api",
            "http": {
                "method": "GET",
                "path": "/Dev/users/message",
                "protocol": "HTTP/1.1",
                "sourceIp": "220.240.78.250",
                "userAgent": "PostmanRuntime/7.29.2",
            },
            "requestId": "WK51UjBzSwMEJDQ=",
            "routeKey": "ANY /users/{proxy+}",
            "stage": "Dev",
            "time": "01/Aug/2022:06:18:09 +0000",
            "timeEpoch": 1659334689888,
        },
        "pathParameters": {"proxy": "message"},
        "isBase64Encoded": False,
    }


def test_get_message(handler: Callable, get_message_event: Mapping) -> None:
    result = handler(get_message_event, MockLambdaContext())
    assert result["statusCode"] == 200 and result["body"] == json.dumps(
        {"message": "Hello World!"}
    )
