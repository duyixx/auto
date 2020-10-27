a = '{"pwd":"12345678","type":1}'

# 判断是不是一个 json, 可以到网上找 json 工具

# b 不是 json，要用双引号
b = "{'pwd':'12345678','type':1}"

# Json 表示数据为空是 null， 不是 None
c = '{"mobile_phone":null, "pwd":"12345678","type":1}'

# 布尔类型 是 true 不是 True
d = '{"mobile_phone":true, "pwd":"12345678","type":1}'

# 为什么要把 json 格式的字符串转化成字典
# d_dict = eval('{"mobile_phone":true, "pwd":"12345678","type":1}')
import json
print(json.loads('{"mobile_phone":true, "pwd":"12345678","type":1}'))