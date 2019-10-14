class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['left','rigth']
    def __init__(self, a,b):
        self.value = Value
    def __reper__(self) :
        return f'Val({self.value})'
    def eval(self):
        return self.value
v = Val(1)
print(v)
assert v.eval() == 1

assert isinstance(v, Expr)
assert isinstance(v, Val)
assert isinstance(v, int)


e = Add(Val(1),Val(2))
assert e.eval() == 3
e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6

class Add(Expr):
    __slots__ = ['left','right']
    def __init__(self,a,b):
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()

e = Add(Val(1),Val(2))
assert e.eval() == 3

e = Add(Val(1),Add(Val(2),Val(3)))
assert e.eval() == 6

print()
print()