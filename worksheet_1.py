a = 15          #Variable Declaration and Types
b = 12

print(type(a))
print(type(b))

print(a + b)    #Basic Arithmetic Operations
print(a - b)
print(a * b)
print(a / b)

c = int(a / b)  #Variables and Type Casting

print(c)
print(type(c))

c = float(c)

print(c)
print(type(c))

message = "The result  of a divided by b is? "
c = float(int(a / b))

print(message + str(c))

# Compare a and b
a = 15
b = 12

print(a > b)
print(a == b)