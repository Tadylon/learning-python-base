class MyClass:
    pass

print(dir(MyClass))
# 输出中包含 '__init__', '__str__', '__repr__', '__eq__' 等
# 这些都是从 object 继承来的默认方法
# 但注意：没有 '__add__', '__getitem__', '__len__'


class GoodPractice:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"GoodPractice({self.value})"
    
    # 即使只是想要基本的相等比较，显式写出来也更清晰
    def __eq__(self, other):
        if not isinstance(other, GoodPractice):
            return False
        return self.value == other.value


gp1 = GoodPractice(10)

repr(gp1)  # 输出: GoodPractice(10)
print(repr(gp1))  # 输出: GoodPractice(10)
gp1.__eq__(GoodPractice(10))  # 输出: True
print(gp1 == GoodPractice(10))  # 输出: True
print(gp1.__eq__(GoodPractice(10)))