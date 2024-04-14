import json


def modify_json(field, value):
    f = open("resources/j.json", "r")
    jsons = f.read()
    jsons = jsons.replace("\"" + field + "\":0", "\"" + field + "\":" + value)
    jsn = json.loads(jsons)
    return jsn
