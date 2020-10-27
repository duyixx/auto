class Handler:
    a = 1
    b = 2


print(Handler.a)

key = "c"
print(getattr(Handler, key, "hello"))