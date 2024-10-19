import itertools

def generate_combinations():
    combinations = list(itertools.product(range(1, 6), range(1, 6), range(1, 5)))
    
    return combinations

combinations = generate_combinations()
for combo in combinations:
    print(combo[0], combo[1], combo[2])

