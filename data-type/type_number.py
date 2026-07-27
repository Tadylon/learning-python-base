import numpy as np

v = np.array([3, 4])   # 这是一个真正的向量
w = np.array([1, 2])

# 支持索引
print(v[0])  # 输出 3

# 支持点积（内积）
print(np.dot(v, w))  # 输出 11

# 支持逐元素乘法（哈达玛积）
print(v * w)  # 输出 [3 8]

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))


x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z)) 

x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z)) 





x = 3+5j
y = 5j
z = -5j

print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z)) 


x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 
print(c.real)  # 输出 3.0
print(c.imag)  # 输出 4.0