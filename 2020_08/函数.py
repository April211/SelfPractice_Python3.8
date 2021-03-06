
# 无参数式函数
def say_hello():
    # 该块属于这一函数
    print('Hello, World!')
# 函数结束

# 带参数的函数
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')
# 函数结束

# 带有默认参数
def say(message, times = 1):
    print(message* times)
# 函数结束


say_hello()  # 调用函数
say_hello()  # 再次调用函数

say('Hello')
say('World', 5)

# 直接传递字面值
print_max(3, 4)

x = 5
y = 7

# 以参数的形式传递变量
print_max(x, y)
