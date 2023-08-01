import random
from time import time
start = time()

def choices():
    options=['heads','tails']
    a= random.choice(options)
    

    return a
result= choices()

print(result)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)