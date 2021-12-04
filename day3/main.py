#pt 1

with open('input.txt', 'r') as f:
    one_counts = None
    lines = 0
    for line in f:
        line = line.strip()
        lines += 1
        if not one_counts:
            one_counts = [0] * len(line)
        for i in range(len(line)):
            if line[i] == '1':
                one_counts[i] += 1

    gamma = epsilon = ''
    thresh = lines // 2
    for count in one_counts:
        if count > thresh:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    print(gamma, epsilon)
    g = int('0b'+gamma, 2)
    e = int('0b'+epsilon, 2)
    print(f"{g} {e} {g*e}")

#pt 2

# o is True means keep 1 values on a tie, co2 keep 0 values on tie
def findRateFrom(nums, isO):
    positions = len(nums[0])
    pos = 0
    while len(nums) > 1 and pos < positions:
        # get mode for pos
        one_counts = 0
        for num in nums:
            if num[pos] == '1':
                one_counts += 1
    
        thresh = len(nums) / 2
        mode = None
        if one_counts > thresh:
            mode = '1' if isO else '0'
        elif one_counts < thresh:
            mode = '0' if isO else '1'
        else: #equal
            mode = '1' if isO else '0'
        
        # filter nums
        nums = list(filter(lambda n: n[pos] == mode, nums))

        pos += 1
    return int('0b' + nums[0], 2)


with open('input.txt', 'r') as f:
    nums = list(map(str.strip, f.readlines()))

    co2 = findRateFrom(nums.copy(), False)
    o2 = findRateFrom(nums.copy(), True)
    
    print('final answer', co2 * o2)
