
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a :str = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 
print(a[0:5]) # prints 'Lorem'
print(a[5:])
print(len(a)) # prints 123


for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

a = "Hello"
b = "World"
c = a + " " + b
print(type(a))
print(type(b))
print(type(c))
print(c)

# 这是测试formatting的代码
age = 36
txt = f"My name is John, and I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = f"We are the so-called \"Vikings\" from the north."
print(txt)
