import multiprocessing
import os
import threading


def EvenDisplay(No):
    print("PID even process :",os.getpid())
    print("list of even no :")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
   

def OddDisplay(No):
    print("PID odd process :",os.getpid())
    print("lisy odd no")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
    

def main():
    print("PID main process :",os.getpid())
    print("Enter number : ")
    value= int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (value,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (value,))

    p1.start()
    p1.join()
 
   

    p2.start()
    p2.join()
   

    print("end of main process")

 

# Starter
if __name__ == "__main__":
    main()