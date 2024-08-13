# Define two numbers for demonstration
a = 10
b = 5

# Arithmetic Operators
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print(f"Floor Division: {a} // {b} = {a // b}")

# Comparison Operators
print(f"Equal: {a} == {b} is {a == b}")
print(f"Not Equal: {a} != {b} is {a != b}")
print(f"Greater than: {a} > {b} is {a > b}")
print(f"Less than: {a} < {b} is {a < b}")
print(f"Greater than or equal to: {a} >= {b} is {a >= b}")
print(f"Less than or equal to: {a} <= {b} is {a <= b}")

# Logical Operators
print(f"Logical AND: {a > 5 and b < 10} (both conditions true)")
print(f"Logical OR: {a > 5 or b > 10} (one condition true)")
print(f"Logical NOT: not({a > 5}) is {not(a > 5)}")

# Bitwise Operators
print(f"Bitwise AND: {a} & {b} = {a & b}")
print(f"Bitwise OR: {a} | {b} = {a | b}")
print(f"Bitwise XOR: {a} ^ {b} = {a ^ b}")
print(f"Bitwise NOT: ~{a} = {~a}")
print(f"Left Shift: {a} << 2 = {a << 2}")
print(f"Right Shift: {a} >> 2 = {a >> 2}")

# Assignment Operators
c = a + b
print(f"Assignment: c = a + b -> c = {c}")
c += a
print(f"Add and assign: c += a -> c = {c}")
c -= b
print(f"Subtract and assign: c -= b -> c = {c}")
c *= a
print(f"Multiply and assign: c *= a -> c = {c}")
c /= b
print(f"Divide and assign: c /= b -> c = {c}")
c %= a
print(f"Modulus and assign: c %= a -> c = {c}")
c **= 2
print(f"Exponent and assign: c **= 2 -> c = {c}")
c //= 3
print(f"Floor divide and assign: c //= 3 -> c = {c}")

# Identity Operators
print(f"Identity: a is b -> {a is b}")
print(f"Identity: a is not b -> {a is not b}")

# Membership Operators
my_list = [1, 2, 3, 4, 5]
print(f"Membership: 3 in my_list -> {3 in my_list}")
print(f"Membership: 6 not in my_list -> {6 not in my_list}")
