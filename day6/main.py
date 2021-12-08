#pt1

with open('input.txt', 'r') as f:
    fish_ages = {i:0 for i in range(9)}
    days = 256

    # fill in starting fish ages
    starting = map(int, f.readline().split(','))
    for age in starting:
        fish_ages[age] += 1

    # age them fish
    for _ in range(days):
        og_due_fish = fish_ages[0]
        for d in range(1, len(fish_ages)):
            fish_ages[d-1] += fish_ages[d]
            fish_ages[d] = 0

        # account for birthed fishes
        fish_ages[len(fish_ages)-1] += og_due_fish
        fish_ages[len(fish_ages)-3] += og_due_fish
        fish_ages[0] -= og_due_fish

    print(sum(fish_ages.values()))
