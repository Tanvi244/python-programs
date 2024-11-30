
import os
import threading


def EvenDisplay(No):
    print("list of even no :")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2
   

def OddDisplay(No):
    print("lisy odd no")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2
    

def main(): 
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