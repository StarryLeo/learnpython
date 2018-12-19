def by_name(t):
    x, y = t
    return x.lower()

def by_score(t):
    x, y = t
    return y

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L1 = sorted(L, key=by_name)
print(L1)

L2 = sorted(L, key=by_score, reverse=True)
print(L2)
