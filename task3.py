from prettytable import PrettyTable
def print_csv(input):
    table = PrettyTable()
    lines = input.split('\n')
    head = lines[0]
    table.field_names = head.split(',')
    for i in range(1, len(lines)):
        table.add_row(lines[i].split(','))
    print(table)
print_csv("a,b\n1,2")