import re

def CheckPassword(pass_):
    totalScore = uniqueness(pass_) + length(pass_) + diversity(pass_) # total score of password, where 100 is the best possible and 30 is the worst possible
    return totalScore

def uniqueness(pass_): # Check uniqueness of the password string, score 40 - no repeating symbols; score 15 - more than 50% of the password is the same symbol
    temp = ''.join(set(pass_))
    score = 40
    for i in range(10,5,-1):
        if len(temp) >= len(pass_) * i/10: return score
        else: score -= 5
    return score

def length(pass_): # Check the length of the password string, score 35 - length of 20; score 15 - length of 8
    score = 35
    for i in [20, 12, 8]:
        if len(pass_) == i: return score
        else: score -= 10

def diversity(pass_): # Check diversity of the password string, score 24 - maximum diversity, score 0 - no diversity
    [u_, l_, n_, s_] = [len(re.sub(i,"",pass_)) for i in ["[^A-Z]", "[^a-z]", "[^0-9]", "[^\W]"]]
    ref = len(pass_)
    score = 0
    for i in [u_, l_, n_, s_]:
        for j in range(55,25,-5):
            if (i < ref * j/100) & (i != 0): score += 1
    return score

