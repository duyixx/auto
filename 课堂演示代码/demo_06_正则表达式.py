"""
regular expression ==> re ==> 正则表达式 regx
"""

import re

# my_string = "xiaolingwangle"
#
# # match
# # \n \t
# # TODO: 正则表达式通常在匹配方式前加r, r"a\w"
# # TODO: 正则表达式当中不要随便加空格；
# print("ab\n")
# print(r"ab\n")


# 三个方法
# my_string = "xiaolingwangleli"
#
# # match 一定要从最开始的地方匹配
# print(re.match(r"ling", my_string))
# # search， 可以在任意地方匹配
# res = re.search(r"li", my_string)
# # print(res.start())
# # print(res.end())
# print(res.group())
# # find_all
#
# print(re.findall(r"li", my_string))


# . 表示：匹配一个字符， 除了\n
my_string = "xiaolingwangleli"
print(re.search(r".", my_string))  #x

# a.
print(re.search(r"a.", my_string))

# [] 代表匹配里面的某一个 [abc] a 或者b 或者 c
print(re.search(r"[oxe]", my_string))

# print(re.search(r"[(li)|(wa)]", my_string))

# \d 表示匹配一个数字， \D 表示非数字
mystring = "_xiao@lingggg25wangleli"
print(re.search(r"\d", mystring))
print(re.search(r"\D", mystring))
# 和 \d 等价
print(re.search(r"[0-9]", mystring))


# \w 大小写字母数字加上_ python 变量命名 ,  \W
print(re.search(r"\w\w\w", mystring))
print(re.search(r"\W", mystring))

# *:前面字符任意次
# print(re.search(r"\d*", mystring))

# # 极可能多的匹配, 贪婪模式
print(re.search(r"\d+?", mystring))

# ? 用法是表示非贪婪模式
# print(re.search(r"?", mystring))

# {m}
print(re.search(r"g{2}", mystring))

print(re.search(r"g{2,}?", mystring))















login_data = '{"member_id": #member_id#,"amount":"#money#"}'
pattern = r'#.+?#'
print(re.search(pattern, login_data))

# result = re.sub(pattern, "19876", login_data, count=1)
# print(result)
#
# result = re.sub(pattern, "10000", result, count=1)
# print(result)

# 括号表示分组

login_data = '{"member_id": #member_id#,"amount":"#money#"}'
pattern = r'#(.+?)#'

# goup0  #member_id#
print(re.search(pattern, login_data).group(0))

# group1  member_id
# group0 表示匹配的字符
# 除了group0 以外， 表示括号里面的内容，有多少个括号，就多多少个分组
print(re.search(pattern, login_data).group(1))
print(re.search(pattern, login_data).group(2))

#
# Handler.属性的方式访问数据

def replace_label(target):
    """用 data 替换 target 里的标签。
    {"mobile_phone":"*phone*"} ==> {"mobile_phone":"137"}
    """
    pattern = r"#(.*?)#"
    while re.search(pattern, target):
        key = re.search(pattern, target).group(1)
        value = getattr(Handler(), key, '')
        target = re.sub(pattern, value, target, 1)
    return target






# 替换
# 循环操作


















# pattern = r"#.*#"
# print(re.search(pattern, login_data))
#
# pattern = r"#(.*?)#"
# print(re.search(pattern, login_data).group(1))









