def Addition(No1, No2):
    print("inside add fun") #dukan
    Ans = 0
    Ans = No1 + No2
    return Ans


def main():
     print("inside add fun")   #ghar
    print("enter fir no :")
    A = int(input())  

    print("enter sec no :")
    B = int(input())  

    Result = Addition(A,B)

    print("Add is : ",Result)

main()  #starter
print("end of application")

