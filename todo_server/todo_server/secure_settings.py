import os
import json


_cached_settings = {}


def get_setting(filepath, name=None, default=None):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"No such file: '{filepath}'")

    abs_filepath = os.path.abspath(filepath)

    if abs_filepath not in _cached_settings:
        with open(abs_filepath) as f:
            try:
                _cached_settings[abs_filepath] = json.load(f)
            except:
                pass

    if abs_filepath in _cached_settings:
        if name is None:
            return _cached_settings[abs_filepath]
        elif name in _cached_settings[abs_filepath]:
            return _cached_settings[abs_filepath][name]

    return default
