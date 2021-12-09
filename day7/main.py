#pt1

def getDiffAmount(crabs, quant):
    s = 0
    for crab in crabs:
        s += abs(crab-quant)
    return s

def part1():
    with open('input.txt', 'r') as f:
        # sort list
        crabs = sorted(map(int, f.readline().split(',')))
        # get median
        l = len(crabs)
        pos = (l//2)+1
        # check - m +, if either lt m, go that direction
        curr = getDiffAmount(crabs, crabs[pos])
        direction = 0
        if curr > getDiffAmount(crabs, crabs[pos+1]):
            direction = 1
        elif curr > getDiffAmount(crabs, crabs[pos-1]):
            direction = -1
        else:
            # medi is the min
            print(curr)
            return
    
        # while !increasing ++/--
        prev = curr
        pos = pos+direction
        curr = getDiffAmount(crabs, crabs[pos])
        while curr <= prev:
            prev = curr
            pos = pos+direction
            curr = getDiffAmount(crabs, crabs[pos])
        # print sum of diffs from prev
        print(prev)

# pt2

def diffAmount(crabs, quant):
    s = 0
    for crab in crabs:
        n = abs(crab-quant)
        s += (n*(n+1)) / 2
    return s

def part2():
    with open('input.txt', 'r') as f:
        # sort list
        crabs = sorted(map(int, f.readline().split(',')))
        # get median
        l = len(crabs)
        pos = (l//2)+1
        # check - m +, if either lt m, go that direction
        curr = diffAmount(crabs, crabs[pos])
        direction = 0
        if curr > diffAmount(crabs, crabs[pos+1]):
            direction = 1
        elif curr > diffAmount(crabs, crabs[pos-1]):
            direction = -1
        else:
            # medi is the min
            print(curr)
            return
    
        # while !increasing ++/--
        prev = curr
        pos = pos+direction
        curr = diffAmount(crabs, crabs[pos])
        while curr <= prev:
            prev = curr
            pos = pos+direction
            curr = diffAmount(crabs, crabs[pos])
        # print sum of diffs from prev
        print(prev)

part2()
