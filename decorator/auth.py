from functools import wraps
from utils.cookie import get_token
from dto.response import make_json_fail

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not get_token():
            return make_json_fail('login required')
        return func(*args, **kwargs)
    return wrapper