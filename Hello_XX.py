from math import sqrt

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))

d = {'x':1, 'y':2, 'z':3}
for key in d:
    print(key,'corresponds to', d[key])

# for n in range(99, 49, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print("didn't find it")

scope = {}
# exec('sqrt = 1', scope)
# print(sqrt(4))
# print(scope['sqrt'])
eval('1+2', scope)
print(scope.keys())