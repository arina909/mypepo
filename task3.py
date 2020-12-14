def print_csv(input):
    from prettytable import PrettyTable
    x = PrettyTable()
    lines = input.split('\n')
    head = lines[0]
    x.field_names = head.split(',')
    n = len(lines)
    for i in range(1, n):
        x.add_row(lines[i].split(','))
    print(x)
print_csv("a,b\n1,2")