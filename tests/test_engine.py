from engine import Value

def test_multiplication_gradient():
    a = Value(2.0)
    b = Value(3.0)

    c = a * b
    c.backward()

    assert a.grad == 3.0
    assert b.grad == 2.0

def test_addition_gradient():
    a = Value(2.0)
    b = Value(3.0)

    c = a + b
    c.backward()

    assert a.grad == 1.0
    assert b.grad == 1.0