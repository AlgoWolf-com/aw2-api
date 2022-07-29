import os
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

cognito_app_client_id = os.environ["COGNITO_APP_CLIENT_ID"]
cognito_idp_client = boto3.client("cognito-idp", os.environ["AWS_REGION"])


def auth_username_password(username, password):
    logger.debug("Entered auth_username_password")
    res = cognito_idp_client.initiate_auth(
        ClientId=cognito_app_client_id,
        AuthFlow="USER_PASSWORD_AUTH",
        AuthParameters={"USERNAME": username, "PASSWORD": password},
    )
    if "AuthenticationResult" in res:
        return res["AuthenticationResult"]["AccessToken"]
    raise Exception("Unable to retrieve access token")


class Query:
    @staticmethod
    def hello(*_):
        logger.debug("Entered hello")
        return "Hello World!"

    @staticmethod
    def login(_, args, __):
        username = args["input"]["email"]
        password = args["input"]["password"]
        return auth_username_password(username, password)

    @staticmethod
    def signup(_, __, ___):
        return "TODO"
