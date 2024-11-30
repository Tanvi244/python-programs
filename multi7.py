
import os
import threading


def EvenDisplay(No):
    print("PID even process :",os.getpid())
    print("even thread",threading.get_ident())
    print("list of even no :")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
   

def OddDisplay(No):
    print("PID odd process :",os.getpid())
    print("pid odd thread",threading.get_ident())
    print("lisy odd no")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
    

def main():
    print("PID main process :",os.getpid())
    print("tid :",threading.get_ident())
    print("Enter number : ")
    value= int(input())

    p1 = threading.Thread(target = EvenDisplay, args = (value,))
    p2 = threading.Thread(target = OddDisplay, args = (value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
   
 
   

   

    print("end of main process")

 

# Starter
if __name__ == "__main__":
    main()