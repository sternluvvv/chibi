from exp import Val

def parse(s: str):
        num = int(s)
        return Val(num)

e = parse("123")
print(e)

s = "1+2"
pos = s.find('+')
print('pos',pos)

s1 = s[0:pos]
s2 = s[pos+1:]
print(s1,s2)

