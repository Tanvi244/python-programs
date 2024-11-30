import os
import multiprocessing

def Task1(No):
    print("execute first task")
    print("pid task1:",os.getpid())#2 khalcha line logic
    print("ppid task1:",os.getppid())


    
def Task2(No):
    print("execute first task")
    print("pid task2:",os.getpid())#logic
    print("ppid task2:",os.getppid())

def main():
    print("pid running process:",os.getpid())
    print("pid process command :",os.getppid())

    value = 11
    p1 = multiprocessing.process(target = Task1,args = (value,))
    p2 = multiprocessing.process(target = Task1,args = (value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()