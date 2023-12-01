import os
import random

def generate_random_set_as_list(n, lower, upper, seed, is_write):
    random_set = set()
    random.seed(seed)

    while len(random_set) < n:
        random_element = random.randint(lower, upper)
        random_set.add(random_element)
    
    # akan berurut hasilnya
    result = list(random_set)
    
    # coba acak
    random.shuffle(result)
    
    if is_write:
        write_list_to_file(result, seed)
    
    return result

def write_list_to_file(lst, seed):
    filename = f"{len(lst)}_elements_seed_{seed}.txt"
    with open(filename, "w") as file:
        for num in lst:
            file.write(str(num) + "\n")