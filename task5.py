def integer(i):
    if type(i) == str:
        try:
            x = int(i)
            print(x)
        except Exception as e:
            print("SpecialBlaException: Impossible to convert")
integer('   ')