import json
from flask import request

from src import main


def health():
    status = "OK"
    code = 200

    return json.dumps(status), code


def register_user_data():
    ret_json = {
        "message": "OK!",
        "status": "success"
    }
    code = 200

    try:
        payload = request.json
        userdata_db = main.database["owe"]["user_data"]
        insertion_return = userdata_db.insert_one(payload)

    except Exception as exc:
        ret_json['message'] = str(exc)
        code = 400

    return ret_json, code
