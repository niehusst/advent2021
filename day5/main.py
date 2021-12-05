# pt 1
def p1():
    with open('input.txt', 'r') as f:
        mapp = [[0 for j in range(1000)] for i in range(1000)]
        for line in f:
            c1, c2 = line.split(' -> ')
            x1,y1 = map(int, c1.split(','))
            x2,y2 = map(int, c2.split(','))
            
            # check not diag
            if x1 == x2:
                # vert
                m = max(y1,y2)
                # mark vents 
                for i in range(min(y1,y2), m+1):
                    mapp[i][x1] += 1
    
            elif y1 == y2:
                # horz
                for i in range(min(x1,x2), max(x1,x2)+1):
                    mapp[y1][i] += 1
            else: #diag
                pass
    
        # count marked vents
        intersections = 0
        for r in range(len(mapp)):
            for c in range(len(mapp[0])):
                intersections += 1 if mapp[r][c] > 1 else 0
    
        print(intersections)

# pt 2
def p2():
    with open('input.txt', 'r') as f:
        mapp = [[0 for j in range(1000)] for i in range(1000)]
        for line in f:
            c1, c2 = line.split(' -> ')
            x1,y1 = map(int, c1.split(','))
            x2,y2 = map(int, c2.split(','))
            
            # check not diag
            if x1 == x2:
                # vert
                m = max(y1,y2)
                # mark vents 
                for i in range(min(y1,y2), m+1):
                    mapp[i][x1] += 1
            elif y1 == y2:
                # horz
                for i in range(min(x1,x2), max(x1,x2)+1):
                    mapp[y1][i] += 1
            else: #diag
                # determine direction
                if x2 < x1:
                    # swap so we always go to right
                    x1,x2,y1,y2 = x2,x1,y2,y1

                # are we going up or down?
                off = 0
                for c in range(x1, x2+1):
                    mapp[y1+off][c] += 1
                    off = off+1 if y1<y2 else off-1

        # count marked vents
        intersections = 0
        for r in range(len(mapp)):
            for c in range(len(mapp[0])):
                intersections += 1 if mapp[r][c] > 1 else 0
    
        print(intersections)

p2()

