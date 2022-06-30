import re

def CheckPassword(pass_):
    totalScore = uniqueness(pass_) + length(pass_) + diversity(pass_)
    return totalScore

def uniqueness(pass_):
    temp = ''.join(set(pass_))
    score = 40
    for i in range(10,5,-1):
        if len(temp) >= len(pass_) * i/10: return score
        else: score -= 5
    return score

def length(pass_):
    score = 35
    for i in [20, 12, 8]:
        if len(pass_) == i: return score
        else: score -= 10

def diversity(pass_):
    [u_, l_, n_, s_] = [len(re.sub(i,"",pass_)) for i in ["[^A-Z]", "[^a-z]", "[^0-9]", "[^\W]"]]
    ref = len(pass_)
    score = 0
    for i in [u_, l_, n_, s_]:
        for j in range(55,25,-5):
            if (i < ref * j/100) & (i != 0): score += 1
    return score

