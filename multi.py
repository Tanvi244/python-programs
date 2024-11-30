


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

   EvenDisplay(value)
   OddDisplay(value)
  
 

# Starter
if __name__ == "__main__":
    main()