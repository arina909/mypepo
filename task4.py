def maximum(string):
    m = 1
    max = 1
    for i in range(0, len(string)-1):
        if (string[i] == string[i+1]):
            m += 1
        else:
            if m > max:
                max = m
                m = 1
    if m > max:
        max = m
    print(max)
maximum('cccgkflokhogfffff')