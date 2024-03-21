# Order of function arguments are as follow
# 1. Positional
# 2. Keyword / Default
# 3. *args
# 4. **kwargs


def addition(a, b, c, d=1, e=2, f=3, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(f)  # 6
    print(args)  # 7, 8, 9, 10
    print(kwargs)  # {x: 11, y: 12, z: 13}
    

addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, x=11, y=12, z=13)