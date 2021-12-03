#part 1
curr = prev = None
count = 0
with open("input.txt", "r") as f:
    raw_in = f.readline()
    curr = int(raw_in) if raw_in else None
    while curr:
        if prev and prev < curr:
            count += 1
        prev = curr
        raw_in = f.readline()
        curr = int(raw_in) if raw_in else None
print(count)

#part 2
curr = 4
prev = 3
count = 0
with open("input.txt", "r") as f:
    arr = list(filter(lambda x: x != None, map(lambda x: int(x) if x else None, f.readlines())))
    while curr <= len(arr):
        count += 1 if sum(arr[curr-3:curr]) > sum(arr[prev-3:prev]) else 0
        curr += 1
        prev += 1
print(count)
