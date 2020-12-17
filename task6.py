def myrange(n):
    if n >= 0:
        i=0
        while i <= n:
            yield i
            i += 1
for i in myrange(9):
    print(i)
