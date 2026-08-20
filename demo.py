from engine import Value

a = Value(2.0)
b = Value(3.0)
c = Value(10.0)

d = a * b
e = d + c

e.backward()

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)