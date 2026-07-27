from typing import Callable

# 这是一个最简单的装饰器
def my_decorator(func : Callable) -> Callable:
    def wrapper():
        print("在函数执行前做点事")
        func()
        print("在函数执行后做点事")
    return wrapper

# 使用装饰器（语法糖）
@my_decorator
def say_hello():
    print("Hello!")

# 上面的 @ 写法等同于：say_hello = my_decorator(say_hello)
say_hello()


def repeat(times : int):
    def decorator(func : Callable[..., None]) -> Callable[..., None]:
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

greet("Alice")  # 会打印三次