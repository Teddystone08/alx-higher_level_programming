#!/usr/bin/python3


import json


def to_json_string(my_obj):
    """
    Converts an object to a JSON string representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        A string that represents the JSON serialization of the object.

    Raises:
        Any exception raised by the `json.dumps()` methdo,
        if the object cannot be serialized to JSON.
    """
    return json.dumps(my_obj)
