import time
import tracemalloc
from partition import check_partition_bnb, check_partition_dp
from random_generator import generate_random_set_as_list

def do_profiling_bnb(arr):
    tracemalloc.start()
    start_time = time.time()
    check_partition_bnb(arr)
    end_time = time.time()
    # using peak memory, in KB
    used_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    time_elapsed = (end_time - start_time) * 1000
    used_memory = used_memory / 1024
    print(f"BnB set ukuran {len(arr)} with sum {sum(arr)}, time: {time_elapsed:.5f} ms, peak memory: {used_memory:.5f}")

def do_profiling_dp(arr):
    tracemalloc.start()
    start_time = time.time()
    check_partition_dp(arr)
    end_time = time.time()
    # using peak memory, in KB
    used_memory = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()

    time_elapsed = (end_time - start_time) * 1000
    used_memory = used_memory / 1024
    print(f"DP set ukuran {len(arr)} with sum {sum(arr)}, time: {time_elapsed:.5f} ms, peak memory: {used_memory:.5f}")

if __name__ == '__main__':
    SEED = 2
    # supaya objektif kita akan generate set yang sum-nya genap
    set_10 = generate_random_set_as_list(10, 0, 50, SEED, True)
    set_40 = generate_random_set_as_list(40, 0, 80, SEED, True)
    set_80 = generate_random_set_as_list(80, 0, 200, SEED, True)

    do_profiling_dp(set_10)
    do_profiling_dp(set_40)
    do_profiling_dp(set_80)

    do_profiling_bnb(set_10)
    do_profiling_bnb(set_40)
    do_profiling_bnb(set_80)

