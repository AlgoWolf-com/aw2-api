import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.critical("Function startup")


def handler(event, _):
    logger.info("Event: %s", json.dumps(event))
    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(
            {
                "message": "Hello World",
            }
        ),
    }
