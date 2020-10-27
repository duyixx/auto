import jsonpath
user =  {"data": {"username": "yuz", "pwd": "123456"}}

# 如果匹配不到数据，直接返回 False
print(jsonpath.jsonpath(user, "$.username"))

# 如果匹配到数据，直接得到结果的列表
print(jsonpath.jsonpath(user, "$..username"))

# 多层
# 2 个点表示子孙层级
res = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 13309,
        "leave_amount": 20.0,
        "mobile_phone": "15512345678",
        "reg_name": "小柠檬",
        "reg_time": "2020-06-12 00:28:46.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2020-06-16 21:05:41",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEzMzA5LCJleHAiOjE1OTIzMTI3NDF9.FSOjPQNia8EVM8Q0KGM2lJvWU6G1U6VLdQB2TED8O6nb2r0AYHkCDswqmC_doiSBi-jz30p_FPsePfv6KBtjuA"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}


print(jsonpath.jsonpath(res, "$..token")[0])
print(jsonpath.jsonpath(res, "$..token_type" )[0])
print(jsonpath.jsonpath(res, "$..id")[0])
