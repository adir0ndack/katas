def printer_error(s):
    num = 0
    den = len(s)
    valid = "abcdefghijklm"
    for i in s:
        if i not in valid:
            num+=1
    return str(num) + '/' + str(den)
