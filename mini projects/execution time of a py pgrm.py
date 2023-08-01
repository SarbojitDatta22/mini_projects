from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence is what is danger for this world"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)