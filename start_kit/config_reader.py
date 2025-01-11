import json
import os
from typing import Any


def load_json(json_file: str) -> dict[str, Any]:
    assert os.path.exists(json_file)
    with open(json_file, 'r') as file:
        config = json.load(file)
    return config


def load_config() -> dict[str, Any]:
    return load_json('config.json')


def save_json(data: Any, json_file: str, **kwargs):
    with open(json_file, 'w') as file:
        json.dump(data, file, **kwargs)
