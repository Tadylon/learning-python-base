Python 类中的内置函数（魔术方法/特殊方法）

这些是类中以双下划线开头和结尾的方法（如 __init__）。它们会在特定的操作下被 Python 解释器自动调用，不需要你手动去写 obj.__len__()，而是直接写 len(obj)。


我按功能将它们分为几大类，帮你详细拆解：
1. 对象的生命周期（创建与销毁）

    __new__(cls, ...)：构造方法。用于创建并返回一个新实例。在 __init__ 之前调用。通常用于继承不可变类型（如 int、str）或实现单例模式时重写。

    __init__(self, ...)：初始化方法。这是你最熟悉的，用于给实例的属性赋值。

    __del__(self)：析构方法。当对象被垃圾回收时调用，通常用于释放外部资源（如关闭文件连接），但 Python 有垃圾回收，不太常用。

2. 对象的表现形式（打印、显示）

    __str__(self)：给用户看的字符串。当你 print(obj) 或 str(obj) 时调用。要求可读性强。

    __repr__(self)：给开发者看的字符串。当你直接输入 obj 回车，或使用 repr(obj) 时调用。要求无歧义，通常看起来像创建对象的代码。如果 __str__ 没定义，Python 会拿 __repr__ 代替。

    __format__(self, format_spec)：当使用 format(obj, spec) 或 f-string 中的格式符时调用。

3. 模拟容器类型（像列表、字典一样操作）

    __len__(self)：返回长度。调用 len(obj) 时触发。

    __getitem__(self, key)：取值。调用 obj[key] 或切片时触发。

    __setitem__(self, key, value)：赋值。调用 obj[key] = value 时触发。

    __delitem__(self, key)：删除。调用 del obj[key] 时触发。

    __contains__(self, item)：成员检查。调用 item in obj 时触发。

    __iter__(self)：返回迭代器。调用 iter(obj) 或 for i in obj 时触发。如果只定义 __getitem__，Python 会回退使用它来迭代。

4. 模拟数值/运算符（实现向量加减、矩阵运算）

你可以让自定义类的实例支持加减乘除。

    算术运算符：__add__ (+), __sub__ (-), __mul__ (*), __truediv__ (/), __floordiv__ (//), __mod__ (%)。

    比较运算符：__lt__ (<), __le__ (<=), __eq__ (==), __ne__ (!=), __gt__ (>), __ge__ (>=)。注意：如果只定义 __eq__，Python 也会自动推导出 !=，但建议显式定义。

    反向运算符：__radd__。当 a + b 中 a 不支持加法时，会调用 b 的 __radd__。

5. 属性访问控制（拦截点号操作）

    __getattr__(self, name)：当访问 不存在 的属性时触发（非常安全）。

    __getattribute__(self, name)：访问 任何 属性时都会触发（无论存不存在）。使用它要非常小心，很容易引起无限递归。

    __setattr__(self, name, value)：给属性赋值时触发。

    __delattr__(self, name)：删除属性时触发。

6. 可调用对象（让实例像函数一样）

    __call__(self, *args, **kwargs)：实现了这个方法后，实例对象就可以像函数一样被调用：obj()。这在需要保存状态的函数（如带参数的装饰器类）中非常有用。

7. 上下文管理器（with 语句）

    __enter__(self)：进入 with 代码块时调用，返回值会赋给 as 后面的变量。

    __exit__(self, exc_type, exc_val, exc_tb)：退出 with 代码块时调用，无论是否发生异常都会执行。常用于自动释放锁、关闭数据库连接。

8. 辅助类定义（元编程）

    __slots__：这不是方法，而是一个类变量。__slots__ = ('x', 'y') 可以禁止实例创建 __dict__，极大节省内存，并限制只能给 x 和 y 赋值。

















