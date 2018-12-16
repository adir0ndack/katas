def tower_builder(n_floors):
    t = []
    n = n_floors
    for f in range(n_floors):
        n-=1
        t.append(' '*n + '*'*(f*2+1) + ' '*n)
    return t
