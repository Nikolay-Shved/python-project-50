import json


def render_json_format(diff):
    return json.dumps(diff, indent=4)