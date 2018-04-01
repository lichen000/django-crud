import json
import datetime

def json_default(value):
    if isinstance(value, datetime.datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    else:
        return value.__dict__

def doJsonP(obj, callback):

    if (callback is None) or (callback == ""):
        return json.dumps(obj, default=json_default)
    else:
        return callback + "(" + json.dumps(obj, default=json_default) + ")"
