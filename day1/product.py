def product(*x):
    p = 1
    for n in x:
        p = p*n
    return p

print(product(5,6,7))
