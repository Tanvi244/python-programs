import multiprocessing
import os
import time

def Fun(No):
    Sum = 0
    print("PID is",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum


def main():
    starttime = time.time()
    Arr = [1000000, 2000000, 3000000, 40000000, 5000]
    Result = []

    for value in Arr:
        Result.append(Fun(value))


    print(Result)
    endtime = time.time()
    print("time required time :",endtime-starttime)
   


    
if __name__ == "__main__":
    main()