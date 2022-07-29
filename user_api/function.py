import json
import logging
from .resolvers import Query

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.critical("Function initialized")

resolver_map = {"Query": Query}


def handler(event, _):
    logger.debug("Event:\n%s", json.dumps(event, indent=2))

    parent_name = event["info"]["parentTypeName"]
    field_name = event["info"]["fieldName"]
    result = getattr(resolver_map[parent_name], field_name)(
        event["prev"], event["arguments"], event["info"]
    )
    return result
