

# 为什么要把 json 格式的字符串转化成字典
json_data = '{"mobile_phone":true, "pwd":"12345678","type":1}'

import json

# 把 json 数据转化成python 字典
dict_data = json.loads(json_data)
print(dict_data)

# eval()


# 把字典转化成 json 字符串
new_dict_data = {'username': 'yuz', 'password': None, 'female': False}
json_data = json.dumps(new_dict_data)
print(json_data)