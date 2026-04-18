import time
import random

# Generate dataset
data_sizes = [5000, 10000, 20000]

def generate_data(size):
    return [random.randint(1, 100000) for _ in range(size)]

# -------- Unoptimized Approach --------
def find_duplicates_list(data):
    duplicates = []
    for i in range(len(data)):
        if data[i] in data[i+1:]:
            duplicates.append(data[i])
    return duplicates

# -------- Optimized Approach --------
def find_duplicates_set(data):
    seen = set()
    duplicates = set()
    
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

# -------- Performance Testing --------
print("Performance Comparison:\n")

for size in data_sizes:
    data = generate_data(size)

    start = time.time()
    find_duplicates_list(data)
    list_time = time.time() - start

    start = time.time()
    find_duplicates_set(data)
    set_time = time.time() - start

    print(f"Data Size: {size}")
    print(f"List Time: {list_time:.4f} sec")
    print(f"Set Time: {set_time:.4f} sec\n")