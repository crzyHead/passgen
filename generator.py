from time import time

def lcg(x, a, c, m):
    while True:
        x = (a * x + c) % m
        yield x


def random_uniform_sample(n, interval, seed=0):
    a, c, m = 1103515245, 12345, 2 ** 31
    bsdrand = lcg(seed, a, c, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (2 ** 31 - 1)) + lower
        sample.append(round(observation))

    return sample

def Generate(let_u=True, let_l=True, sym=True, num=True, length=20):
    seed = int(time() * 1000)
    l_up = {let_u:"ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    l_low = {let_l:"abcdefghijklmnopqrstuvwxyz"}
    _num = {num:"0123456789"}
    _sym = {sym:"~!@#$%^*-_=+[{]}/;:,.?"}
    joined = ""
    for i in [l_up,l_low,_num,_sym]:
        if True in i: joined += i.get(True)
    password = ""
    password += "".join([joined[i] for i in random_uniform_sample(length,[0,len(joined)-1], seed)])
    return password
