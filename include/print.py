
def print_obj(*args, **kwargs):
    """自定义 print 函数，添加前缀"""
    built_in_print = __builtins__.print
    built_in_print("[自定义打印]:", *args, **kwargs)