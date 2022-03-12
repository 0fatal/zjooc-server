def make_json_success(data):
    return {
        'code': 0,
        'msg': 'success',
        'data': data
    }

def make_json_fail(msg: str):
    return {
        'code': -1,
        'msg': msg,
        'data': None
    }