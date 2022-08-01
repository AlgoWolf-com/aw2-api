import json
import logging
from typing import Dict

logger = logging.getLogger(__name__)


class Response:
    def __init__(
        self,
        status_code: int = 200,
        body: Dict = None,
        headers: Dict = None,
        is_base64_encoded: bool = False,
    ) -> None:
        self.status_code = status_code
        self.body = body
        self.headers = headers
        self.is_base64_encoded = is_base64_encoded

    @classmethod
    def ok(  # pylint: disable=invalid-name
        cls, body: Dict = None, headers: Dict = None, is_base64_encoded: bool = False
    ):
        return cls(
            status_code=200,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    @classmethod
    def bad_request(
        cls, body: Dict = None, headers: Dict = None, is_base64_encoded: bool = False
    ):
        return cls(
            status_code=400,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    @classmethod
    def internal_server_error(
        cls, body: Dict = None, headers: Dict = None, is_base64_encoded: bool = False
    ):
        return cls(
            status_code=500,
            body=body,
            headers=headers,
            is_base64_encoded=is_base64_encoded,
        )

    def update_headers(self, header, value):
        if self.headers is None:
            self.headers = {}
        self.headers[header] = value

    def generate_response(self) -> Dict:
        headers = {
            **{
                "Content-Type": "application/json",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "DELETE,GET,HEAD,OPTIONS,PATCH,POST,PUT",
            },
            **({} if self.headers is None else self.headers),
        }
        body = {} if self.body is None else self.body

        return {
            "isBase64Encoded": self.is_base64_encoded,
            "statusCode": self.status_code,
            "headers": headers,
            "body": json.dumps(body),
        }
