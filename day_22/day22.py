import re


def new_stack(stack):
    stack.reverse()
    return stack


def cut_stack(stack, n):
    if n < 0:
        # Negative cut
        cut = stack[n:]
        stack = cut + stack[:n]
    else:
        # Positive cut
        cut = stack[:n]
        stack = stack[n:] + cut
    return stack


def increment_deal(stack, n):
    table = [None] * len(stack)
    table_length = len(table)
    counter = 0
    while stack:
        table[counter] = stack.pop(0)
        new_counter = counter + n

        if new_counter >= table_length:
            overflow = new_counter - table_length
            counter = overflow
        else:
            counter = new_counter
    return table


def new_deck(n):
    return [x for x in range(n)]


with open('day22_input.txt') as f:
    instructions = f.readlines()

cards = new_deck(10007)
regex = re.compile(r'[-]*\d+')
for ins in instructions:
    rg = regex.search(ins)
    num = 0
    if rg:
        num = int(rg.group())

    if ins.startswith('deal with increment'):
        cards = increment_deal(cards, num)
    elif ins.startswith('cut'):
        cards = cut_stack(cards, num)
    else:
        cards = new_stack(cards)

print(cards.index(2019))
