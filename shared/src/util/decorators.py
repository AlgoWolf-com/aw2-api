from functools import wraps
from cattrs import structure


def structure_input(event_class):
    def outer(func):
        @wraps(func)
        def wrapper(event, ctx):
            input_event = structure(event, event_class)
            return func(input_event, ctx)

        return wrapper

    return outer
