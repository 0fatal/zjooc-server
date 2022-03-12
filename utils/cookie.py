from flask import Response, make_response, request


def get_token() -> str:
    c1 = request.cookies.get('atoken')
    c2 = request.cookies.get('lano.connect.sid')
    return f'atoken={c1}; lano.connect.sid={c2}'


def set_token(resp:Response, cookies: str)->Response:
    for cookie in cookies.split(';'):
        k = cookie.split('=')[0].strip()
        v = cookie.split('=')[1].strip()
        resp.set_cookie(k, v)

    return resp