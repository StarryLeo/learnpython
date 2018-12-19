from functools import reduce

def str2float(s):
    i = s.find('.')
    s1, s2 = list(map(int, s[:i])), list(map(int, s[i+1:]))
    r1, r2 = reduce(lambda x,y: 10*x+y, s1), reduce(lambda x, y: 0.1*x+y,s2[::-1])*0.1
    return r1 + r2

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
