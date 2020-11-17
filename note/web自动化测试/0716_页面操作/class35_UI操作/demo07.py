
_actions = []

def move_to():
    print("移动。。。")

def click():

    print("点击")


_actions.append(click)
_actions.append(move_to)


def perform():
    for action in _actions:
        action()

perform()

# 数据库操作， ORM ， where, order_by, limit, offset


