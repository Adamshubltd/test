import random
symbol_count = {'A':2, 'B':4, 'C':6, 'D':8}

def generate_slot_machine(rows, cols, symbols):
    all_symbol = []
    for k, v in symbol_count.items():
        for _ in range(v):
            all_symbol.append(k)

    columns = []
    for _ in range(cols):
        column = []
        new_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(new_symbol)
            new_symbol.remove(value)
            column.append(value)
        columns.append(column)
    print(columns)


print(type(generate_slot_machine(3, 3, symbol_count)))
