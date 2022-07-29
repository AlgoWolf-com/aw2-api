# pylint: disable=redefined-outer-name,import-outside-toplevel
import os
from unittest import mock
from typing import Callable, Mapping
import pytest


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
def hello_event() -> Mapping:
    return {
        "arguments": {},
        "identity": None,
        "source": None,
        "request": {
            "headers": {
                "x-forwarded-for": "103.1.56.45, 130.176.212.8",
                "sec-ch-ua-mobile": "?0",
                "cloudfront-viewer-country": "AU",
                "cloudfront-is-tablet-viewer": "false",
                "x-amzn-requestid": "8c5a496c-0cbd-4074-b231-440709f5777c",
                "via": "2.0 d565d9b03fa73bc2ae98eaadac0992b6.cloudfront.net (CloudFront)",
                "cloudfront-forwarded-proto": "https",
                "origin": "https://ap-southeast-2.console.aws.amazon.com",
                "content-length": "150",
                "x-forwarded-proto": "https",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "host": "pszdwi27krchhe2m7synyvpyi4.appsync-api.ap-southeast-2.amazonaws.com",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                "cloudfront-is-mobile-viewer": "false",
                "accept": "application/json, text/plain, */*",
                "cloudfront-viewer-asn": "7545",
                "cloudfront-is-smarttv-viewer": "false",
                "accept-encoding": "gzip, deflate, br",
                "referer": "https://ap-southeast-2.console.aws.amazon.com/",
                "x-api-key": "da2-lhjvk7hnerdqrchdhoaaked2zm",
                "content-type": "application/json",
                "sec-fetch-mode": "cors",
                "x-amzn-trace-id": "Root=1-62e389f5-240eed67347039b632f49009",
                "x-amz-cf-id": "ZCvUvqOdWnsmxdyyhDKXOgMs2GxtpChOBEqJH6KCNnTjbq7UjYP7kQ==",
                "sec-fetch-dest": "empty",
                "x-amz-user-agent": "AWS-Console-AppSync/",
                "sec-ch-ua-platform": '"macOS"',
                "cloudfront-is-desktop-viewer": "true",
                "sec-fetch-site": "cross-site",
                "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                "x-forwarded-port": "443",
            },
            "domainName": None,
        },
        "prev": None,
        "info": {
            "selectionSetList": [],
            "selectionSetGraphQL": "",
            "fieldName": "hello",
            "parentTypeName": "Query",
            "variables": {},
        },
        "stash": {},
    }


@pytest.fixture
def successful_login_event() -> Mapping:
    return {
        "arguments": {
            "input": {"email": "ethanjohol@gmail.com", "password": "Rxs#aBtD+S&9"}
        },
        "identity": None,
        "source": None,
        "request": {
            "headers": {
                "x-forwarded-for": "103.1.56.45, 130.176.212.8",
                "sec-ch-ua-mobile": "?0",
                "cloudfront-viewer-country": "AU",
                "cloudfront-is-tablet-viewer": "false",
                "x-amzn-requestid": "8c5a496c-0cbd-4074-b231-440709f5777c",
                "via": "2.0 d565d9b03fa73bc2ae98eaadac0992b6.cloudfront.net (CloudFront)",
                "cloudfront-forwarded-proto": "https",
                "origin": "https://ap-southeast-2.console.aws.amazon.com",
                "content-length": "150",
                "x-forwarded-proto": "https",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "host": "pszdwi27krchhe2m7synyvpyi4.appsync-api.ap-southeast-2.amazonaws.com",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                "cloudfront-is-mobile-viewer": "false",
                "accept": "application/json, text/plain, */*",
                "cloudfront-viewer-asn": "7545",
                "cloudfront-is-smarttv-viewer": "false",
                "accept-encoding": "gzip, deflate, br",
                "referer": "https://ap-southeast-2.console.aws.amazon.com/",
                "x-api-key": "da2-lhjvk7hnerdqrchdhoaaked2zm",
                "content-type": "application/json",
                "sec-fetch-mode": "cors",
                "x-amzn-trace-id": "Root=1-62e389f5-240eed67347039b632f49009",
                "x-amz-cf-id": "ZCvUvqOdWnsmxdyyhDKXOgMs2GxtpChOBEqJH6KCNnTjbq7UjYP7kQ==",
                "sec-fetch-dest": "empty",
                "x-amz-user-agent": "AWS-Console-AppSync/",
                "sec-ch-ua-platform": '"macOS"',
                "cloudfront-is-desktop-viewer": "true",
                "sec-fetch-site": "cross-site",
                "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                "x-forwarded-port": "443",
            },
            "domainName": None,
        },
        "prev": None,
        "info": {
            "selectionSetList": [],
            "selectionSetGraphQL": "",
            "fieldName": "login",
            "parentTypeName": "Query",
            "variables": {},
        },
        "stash": {},
    }


@pytest.fixture
def undefined_query_event() -> Mapping:
    return {
        "arguments": {},
        "identity": None,
        "source": None,
        "request": {
            "headers": {
                "x-forwarded-for": "103.1.56.45, 130.176.212.8",
                "sec-ch-ua-mobile": "?0",
                "cloudfront-viewer-country": "AU",
                "cloudfront-is-tablet-viewer": "false",
                "x-amzn-requestid": "8c5a496c-0cbd-4074-b231-440709f5777c",
                "via": "2.0 d565d9b03fa73bc2ae98eaadac0992b6.cloudfront.net (CloudFront)",
                "cloudfront-forwarded-proto": "https",
                "origin": "https://ap-southeast-2.console.aws.amazon.com",
                "content-length": "150",
                "x-forwarded-proto": "https",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
                "host": "pszdwi27krchhe2m7synyvpyi4.appsync-api.ap-southeast-2.amazonaws.com",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                "cloudfront-is-mobile-viewer": "false",
                "accept": "application/json, text/plain, */*",
                "cloudfront-viewer-asn": "7545",
                "cloudfront-is-smarttv-viewer": "false",
                "accept-encoding": "gzip, deflate, br",
                "referer": "https://ap-southeast-2.console.aws.amazon.com/",
                "x-api-key": "da2-lhjvk7hnerdqrchdhoaaked2zm",
                "content-type": "application/json",
                "sec-fetch-mode": "cors",
                "x-amzn-trace-id": "Root=1-62e389f5-240eed67347039b632f49009",
                "x-amz-cf-id": "ZCvUvqOdWnsmxdyyhDKXOgMs2GxtpChOBEqJH6KCNnTjbq7UjYP7kQ==",
                "sec-fetch-dest": "empty",
                "x-amz-user-agent": "AWS-Console-AppSync/",
                "sec-ch-ua-platform": '"macOS"',
                "cloudfront-is-desktop-viewer": "true",
                "sec-fetch-site": "cross-site",
                "sec-ch-ua": '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
                "x-forwarded-port": "443",
            },
            "domainName": None,
        },
        "prev": None,
        "info": {
            "selectionSetList": [],
            "selectionSetGraphQL": "",
            "fieldName": "foo",
            "parentTypeName": "Query",
            "variables": {},
        },
        "stash": {},
    }


def test_hello(handler: Callable, hello_event: Mapping) -> None:
    result = handler(hello_event, None)
    assert result == "Hello World!"


def test_successful_login(handler: Callable, successful_login_event: Mapping) -> None:
    result = handler(successful_login_event, None)
    assert isinstance(result, str)


def test_undefined_query(handler: Callable, undefined_query_event: Mapping) -> None:
    try:
        handler(undefined_query_event, None)
        assert False
    except AttributeError:
        assert True
