def maximum(string):
    count = 1
    max = 1
    for i in range(0, len(string)-1):
        if (string[i] == string[i+1]):
            count += 1
        else:
            count = 1
            if count > max:
                max = count
        if count > max:
            max = count
    print(max)
    return max
maximum('ddvvrwwwrgggg')