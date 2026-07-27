from typing import Callable

class CountCalls:
    def __init__(self, func : Callable):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数被调用了 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def test():
    print("执行中")

test()  # 输出：函数被调用了 1 次
test()  # 输出：函数被调用了 2 次