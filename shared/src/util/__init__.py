import json
import pathlib
import logging
import traceback
from typing import Callable, Dict
from functools import wraps
import jsonschema
from jsonschema import validate
from apigw import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_schema(name: str) -> Dict:
    current_dir = pathlib.Path(name).parent.resolve()
    with open(f"{current_dir}/schema.json", "r", encoding="utf-8") as file:
        schema = json.load(file)
    return schema


def validate_json_schema(name: str) -> Dict:
    def outer(func: Callable) -> Dict:
        @wraps(func)
        def wrapper(event, ctx):
            logger.debug("validate_json_schema: %s", json.dumps(event, indent=2))
            schema = get_schema(name)
            try:
                validate(instance=event, schema=schema)
            except jsonschema.exceptions.ValidationError:
                logger.error(traceback.format_exc())
                return Response(
                    status_code=400, body={"error": "Unable to parse body request"}
                ).generate_response()

            return func(event, ctx)

        return wrapper

    return outer


def hide_errors() -> Dict:
    def outer(func: Callable) -> Dict:
        @wraps(func)
        def wrapper(event, ctx):
            try:
                return func(event, ctx)
            except Exception:  # pylint: disable=broad-except
                logger.error(traceback.format_exc())
                return Response(
                    status_code=400, body={"error": "Unable to parse body request"}
                ).generate_response()

        return wrapper

    return outer
