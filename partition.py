def partition_values_from_index(values, start_index, total_value, unassigned_value, 
                                test_assignment, test_value, best_assignment, best_err): 

    if start_index >= len(values): 
        # We're done. See if this assignment is better than what we have so far. 
        test_err = abs(2 * test_value - total_value) 
        if test_err < best_err[0]: 
            # This is an improvement. Save it. 
            best_err[0] = test_err 
            best_assignment[:] = test_assignment[:] 
            #print(f"best error improvement: {best_err[0]}")

    else: 
        # See if there's any way we can assign the remaining items to improve the solution. 
        test_err = abs(2 * test_value - total_value) 
        if test_err - unassigned_value < best_err[0]: 
            # There's a chance we can make an improvement. 
            # We will now assign the next item. 
            unassigned_value -= values[start_index] 

            # Try adding values[start_index] to set 1. 
            test_assignment[start_index] = True 
            #print("test_assignment=true")
            #print(f"partition(start_index={start_index+1}, unassigned_value={unassigned_value}, test_assignment={test_assignment}, test_value={test_value+values[start_index]}, best_assignment={best_assignment}, best_err={best_err[0]})") 
 
            partition_values_from_index(values, start_index + 1, 
                                         total_value, unassigned_value, 
                                         test_assignment, test_value + values[start_index], 
                                         best_assignment, best_err) 
 
            # Try adding values[start_index] to set 2. 
            test_assignment[start_index] = False 
            #print("test_assignment=false")
            #print(f"partition(start_index={start_index+1}, unassigned_value={unassigned_value}, test_assignment={test_assignment}, test_value={test_value}, best_assignment={best_assignment}, best_err={best_err[0]})") 
            partition_values_from_index(values, start_index + 1, 
                                         total_value, unassigned_value, 
                                         test_assignment, test_value, 
                                         best_assignment, best_err) 

def partition_values_from_index_bf(values, start_index, total_value, 
                                test_assignment, test_value, 
                                best_assignment, best_err): 
    # simulasi exhaustive search/brute force
    if start_index >= len(values): 
        # We're done. See if this assignment is better than what we have so far. 
        test_err = abs(2 * test_value - total_value) 
        if test_err < best_err[0]: 
            # This is an improvement. Save it. 
            best_err[0] = test_err 
            best_assignment[:] = test_assignment[:] 
    else: 
        # Try adding values[start_index] to set 1. 
        test_assignment[start_index] = True 
        #print("test_assignment=true")
        #print(f"partition(start_index={start_index+1}, test_assignment={test_assignment}, test_value={test_value+values[start_index]}, best_assignment={best_assignment}, best_err={best_err})") 
        partition_values_from_index_bf(values, start_index + 1, 
                                     total_value, test_assignment, 
                                     test_value + values[start_index], 
                                     best_assignment, best_err) 
        
        # Try adding values[start_index] to set 2. 
        test_assignment[start_index] = False 
        #print("test_assignment=false") 
        #print(f"partition(start_index={start_index+1}, test_assignment={test_assignment}, test_value={test_value}, best_assignment={best_assignment}, best_err={best_err})") 
        partition_values_from_index_bf(values, start_index + 1, 
                                     total_value, test_assignment, test_value, 
                                     best_assignment, best_err) 

def check_partition_dp(arr):
    sum = 0
    i, j = 0, 0
    n = len(arr)
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for _ in range(n + 1)]
            for _ in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1): 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1] 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
    
    # print table
    #for col in part:
    #    print(col)
 
    return part[sum // 2][n]


def check_partition_bnb(values):
    test_assignment = [False] * len(values) 
    best_assignment = [False] * len(values) 
    best_err = [float('inf')]

    partition_values_from_index(values, 0, sum(values), sum(values), test_assignment, 0, best_assignment, best_err) 

    if best_err[0] == 0:
        return True
    return False