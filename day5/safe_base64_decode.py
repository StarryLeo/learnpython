import base64

def safe_base64_decode(s):
    if len(s)%4 == 3:
        s += b'='
    if len(s)%4 == 2:
        s += b'=='
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
