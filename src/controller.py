import json


def health():
    status = "OK"
    code = 200

    return json.dumps(status), code
