#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# email: avgmax@foxmail.com
# wechat: avgmax
# author: JhonSmith

import pymysql
from pymysql.cursors import DictCursor
import redis
import pymongo


class MysqlHandler(object):
    def __init__(self,
                 host="",
                 port=3306,
                 user="",
                 password="",
                 charset='utf8',
                 cursorclass=DictCursor,
                 read_timeout=15,
                 write_timeout=15

                 ):
        self.__mysql = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass,
            read_timeout=read_timeout,
            write_timeout=write_timeout
        )

        self.cursor = self.__mysql.cursor()

    def query(self, sql, one=False):
        """根据sql查询数据"""
        self.__mysql.commit()  # 把最新的数据进行更新（提交事务。）
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.__mysql.close()


class RedisHandler(object):
    def __init__(self,
                 host="",
                 port=6379,
                 auth="",
                 query_wait=30
                 ):
        self.__redis_client = redis.StrictRedis(host=host, port=port, socket_timeout=query_wait,password=auth,db=0)

    def get(self, key):
        """获取对应key的值"""
        if self.__redis_client.exists(key):
            return self.__redis_client.get(key).decode("utf8")
        else:
            return "该键值对不存在"

    def set_key(self, key, value):
        """设置字符串key"""
        self.__redis_client.set(key, value)

    def exists_key(self, key):
        """1：key存在，0：key不存在"""
        return self.__redis_client.exists(key)

    def del_key(self, key):
        self.__redis_client.delete(key)

    def close(self):
        self.__redis_client.close()

    def find_keys(self,query="*"):
        re:list = []
        it=self.__redis_client.keys(pattern=query)
        for item in it:
            re.append(item.decode("utf8"))
        return re


class MongoHandler(object):
    def __init__(self, host=None, port=27017, user=None, password=None,query_waitMs=1500):
        """创建连接mongoDb的套接字, 如果提供了用户名和密码就获取鉴权
        """
        # client=pymongo.MongoClient('mongodb://%s:%s@192.168.0.102:27017' % ('admin', '123456'))
        self.__mongo_client = pymongo.MongoClient(host, port, socketTimeoutMS=query_waitMs)
        if user and password:
            self.__mongo_client['admin'].authenticate(name=user, password=password)

    def get_conllection(self, database_name, collection_name):
        return self.__mongo_client[database_name][collection_name]

    def query(self, database_name, collection_name, select: dict = None):
        """获取集合里的文档，如果提供条件就按条件查询"""
        docs_list = []
        if select:
            docs = self.get_conllection(database_name, collection_name).find(select)
        else:
            docs = self.get_conllection(database_name, collection_name).find()
        for tem in docs:
            docs_list.append(tem)
        return docs_list


if __name__ == '__main__':
    pass
    # db = MysqlHandler(
    #     host="120.78.128.25",
    #     port=3306,
    #     user="future",

    #     password="123456",
    #     charset='utf8',
    #     cursorclass=DictCursor
    # )
    #
    # data = db.query("SELECT * FROM futureloan.member WHERE mobile_phone={} LIMIT 10;".format(13120208090))
    # print(data)
    # db = MysqlHandler(
    #     host="192.168.0.102",
    #     port=3308,
    #     user="root",
    #     password="123456",
    #     charset="utf8",
    #     cursorclass=DictCursor
    # )
    # data = db.query("select * from test.student;")
    # print(data)
    # redis = RedisHandler(
    #     host="192.168.0.102",
    #     port=6379,
    # )
    # print(redis.find_keys())
    # import redis
    # rd = redis.StrictRedis( host="192.168.0.102",
    #     port=6379,password=123456)
    # print(rd.keys())
    # data2 = redis.get("ram")
    # print(data2)
    # redis.set_key("te", 1)
    # print(redis.exists_key("te"))
    # redis.del_key("te")
    # print(redis.exists_key("te"))
    # import pymongo
    # # c = pymongo.MongoClient(host="192.168.0.102", port=27017)
    # mongoc = MongoHandler(host="192.168.0.102", port=27017, user='admin', password='123456')
    # print(1)
    # print(mongoc.query('test', 'stu'))
    # import datetime
    # li1=[]
    # li2=[]
    # st = [x for x in range(100000)]
    # t1=datetime.datetime.now()
    # print("t1",t1)
    # it = iter(st)
    # for x in range(len(st)):
    #     li1.append(it.__next__())
    # t11=datetime.datetime.now()
    # print("t11",t11)
    # print(t11-t1)
    #
    # t2 = datetime.datetime.now()
    # print("t2",t2)
    # for item in it:
    #     li2.append(item)
    # t22=datetime.datetime.now()
    # print("t22",t22)
    # print(t22-t2)


