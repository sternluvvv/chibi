def calc(s):
    print(s)
    nums = map(int, s.split('+'))
    print(list(nums))
    return sum(nums)

print(calc("1+2+3"))