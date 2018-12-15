# without using set
def longest(s1, s2):
    out = ''
    for c in s2:
        if c not in out:
            out = out + c
    for c in s1:
        if c not in out:
            out = out + c
    return ''.join(sorted(out))

# with set
def longest(s1, s2):
    return ''.join(sorted(set(s1+s2)))
    
