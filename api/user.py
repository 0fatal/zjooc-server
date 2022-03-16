from flask import Blueprint, make_response, request
from utils.cookie import get_token, set_token
from internal.core.zjooc import ZJOOC
from dto.response import make_json_success, make_json_fail

userApi = Blueprint('user', __name__)


@userApi.post('/login')
def login():
    try:
        username = request.get_json()['username']
        password = request.get_json()['password']
    except Exception as e:
        print(e)
        return make_json_fail('wrong username or password')

    try:
        zj = ZJOOC.account(username,password)
        cookies = zj.doLogin()
    except:
        return make_json_fail('login fail')

    resp = make_response(make_json_success(None))
    set_token(resp, cookies)

    return resp

