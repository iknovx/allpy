for i in range(5):
    print(f'{i+1} = {i}')
    
for i in range(1, 6):
    print(f'{i} = {i-1}')

for i in range(0, 10, 2):
    print(f'{i} = {i//2}')
res = 1
for i in range(10):
    res += i
    i += res
    print(i)



import time

x: int = int(input("Enter a number to countdown from: "))

for i in range(x, 0-1, -1):
    print(i)
    time.sleep(1)