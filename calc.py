def calc(s):
    print(s)
    nums = map(int, s.split())
    print(nums)
    nums.remove('*')
    print(nums)
    return sum(nums)

print(calc("1*2+3"))