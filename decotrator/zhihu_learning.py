from typing import Callable
from functools import wraps

# https://zhuanlan.zhihu.com/p/588115066

# def func1():
#     print("run func1")

# def prog1(func : Callable) -> None:
#     print("program start")
#     func()


# prog1(func1)  # 输出: program start \n run func1

def prog1(func):
    @wraps(func)
    def wrapfunc():
        print("program start")
        func()
    return wrapfunc

@prog1
def func1():
    print("run func1")

func1()  # 输出: program start \n run func1

print(func1.__name__)  