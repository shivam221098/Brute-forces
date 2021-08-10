import string
from itertools import product

alphabet = string.ascii_lowercase
numbers = string.digits

for j in range(10):
    for i in product(alphabet + numbers, repeat=j):
        print("".join(i))
        if "".join(i) == "java1":
            print("Pattern found", "".join(i))
            exit(0)