import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
# Add the include directory to the Python path
sys.path.append(str(project_root))

from include.print import print_obj

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5


print(x / y)
print(x // y)  # 整除