import numpy as np

with open("data/small.txt") as file:
    small = [list(x.rstrip()) for x in file.readlines()]
    
with open("data/large.txt") as file:
    large = [list(x.rstrip()) for x in file.readlines()]

small_np = np.array(small)
large_np = np.array(large)
