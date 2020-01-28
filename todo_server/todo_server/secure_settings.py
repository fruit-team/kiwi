import os
import json


def get_setting(filepath, name=None, default=None):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No such file: '{filepath}'")

    settings = None

    with open(filepath) as f:
        try:
            settings = json.load(f)
            if name is None:
                return settings
            else:
                if isinstance(settings, dict):
                    return settings.get(name, default)
        except:
            raise Exception(f"Not a vaild json file: '{filepath}'")

    if settings is None:
        raise Exception(f"Not a vaild key-value json file: '{filepath}'")
