import time 
def timer():
    x = int(input("Enter a number to countdown from: "))

    for i in range(x, 0-1, -1):
       time.sleep(1)
       print(f'{i}s')
    
    time.sleep(.5)
    print("time is over")
    
    
    with open("basics_py/projects/logs/countdown.txt", "w") as f:
        f.write(f'Countdown from {x} completed.')