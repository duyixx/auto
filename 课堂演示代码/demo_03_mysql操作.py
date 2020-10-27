import pymysql

# 建立连接
from pymysql.cursors import DictCursor

conn = pymysql.connect(
    host="120.78.128.25",
    port=3306,
    user="future",
    password="123456",
    charset='utf8',
    cursorclass=DictCursor
)

print(conn)
# 初始化游标
cursor = conn.cursor()
print(cursor)

# 执行 sql 语句
res = cursor.execute("SELECT * FROM futureloan.member LIMIT 10;")
print(res)
# 得到查询数据
members = cursor.fetchall()
print(members)

# 得到一条记录
# 在获取一次游标
# cursor2 = conn.cursor()
# cursor2.execute("SELECT * FROM futureloan.member LIMIT 10;")
# member = cursor2.fetchone()
# print(member)

# 游标对象关闭
cursor.close()
# 连接对象关闭
conn.close()


# 游标和我们操作文件光标
# TODO: 一个游标对象，最好只获取一次，获取多次很容易出问题。