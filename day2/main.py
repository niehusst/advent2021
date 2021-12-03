#pt 1
with open('input.txt', 'r') as f:
    x = y = 0

    for line in f:
        cmd, quant = line.split(' ')
        if cmd == 'forward':
            x += int(quant)
        elif cmd == 'down':
            y += int(quant)
        elif cmd == 'up':
            y -= int(quant)

    print(x * y)

#pt 2
with open('input.txt', 'r') as f:
    x = y = aim = 0

    for line in f:
        cmd, quant = line.split(' ')
        if cmd == 'forward':
            x += int(quant)
            y += aim * int(quant)
        elif cmd == 'down':
            aim += int(quant)
        elif cmd == 'up':
            aim -= int(quant)

    print(x * y)
