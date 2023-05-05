
# FizzBuzz
def fz(input, first, second, phrase1, phrase2):
    if input % first == 0 and input % second == 0:
        return phrase1 + phrase2
    elif input % first == 0:
        return phrase1
    elif input % second == 0:
        return phrase2
    else:
        return str(input)
    
# Fibonacci
def fb(x, y, z):
    # first two terms are 0, 1
    result = [0, 1]
    # initialize F(x-n)
    f1 = None
    f2 = None
    for i in range(2, x+1):
        try:
            # F(x-y)
            f1 = result[i - y] 
            # F(x-z)
            f2 = result[i - z]
        # If F(x-n) doesn't exist, output 1
        except IndexError: # For out of index error
            if f1 is None:
                f1 = 1
            if f2 is None:
                f2 = 1
            # add F(x-y) + F(x-z) to result
        result.append(f1 + f2)
    return result


# function for fibonacci numbers
def helper_fb(x, y, z, arr):
    # initialize F(x-n)
    a, b = x-y, x-z
    # 1, 2 in fibonacci sequence outputs 1
    if x in (1,2):
        return 1
    # If F(x-n) doesn't exist, output 1
    try:
        if str(a) not in arr[a]:
            a = 1
        if str(b) not in arr[b]:
            b = 1
    except IndexError: # For out of index error
        a,b = 1, 1
    # swap a w
    for i in range(0, x):
        a, b = b, a+b
    return a

# Combine the Two
def cb(x, y, z, d1, d2, p1, p2):
    # initialize result array with fibonacci sequence
    result = []
    for j in range (1, x):
        result.append(str(helper_fb(j, y, z, result)))
    print(result)
    # apply FizzBuzz on the fibo sequence
    for i in range (1, len(result)):
        if int(result[i]) % d1 == 0 and int(result[i]) % d2 == 0:
            result[i] = (p1 + p2)
        elif int(result[i]) % d1 == 0:
            result[i] = (p1)
        elif int(result[i]) % d2 == 0:
            result[i] = (p2)

    return result