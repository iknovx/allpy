import time 

x = int(input("Enter a number to countdown from: "))

for i in range(x, 0-1, -1):
    print(f'{i}s')
    time.sleep(1)
with open("basic/projects/logs/countdown.txt", "w") as f:
    f.write(f'Countdown from {x} completed.')