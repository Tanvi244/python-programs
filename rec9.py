

i = 1
Fact = 1

def factorial(no):
    global i
    global Fact

    if(no >= 1):
        Fact = Fact * no
        
        no = no - 1
        factorial(no)

    return Fact

    
def main():
    print("enter no:")
    value = int(input())



    Ret =  factorial(value)

    print("factorial: ",Ret)
    


if __name__ == "__main__":
        main()