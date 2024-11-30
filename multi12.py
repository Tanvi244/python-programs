import multiprocessing
import os

def Fun(No):
    Sum = 0
    print("PID is",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum


def main():
    starttime = time.time()
    Arr = [1000, 2000, 3000000, 40000000, 5000]
    Result = []

    p = multiprocessing.pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()



    print(Result)
    endtime = time.time()
    print("time required time :",endtime-starttime)
   


    
if __name__ == "__main__":
    main()