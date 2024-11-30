print("demo of procedural")

def Addition(No1,No2):
    Ans = No1 + No2
    return Ans

def subtraction(No1,No2):
    Ans = No1 - No2
    return Ans

def main():
    print("enter first no:")
    A = int(input())

    print("enter sec no :")
    B = int(input())

    Ret = Addition(A,B)
    print("addition is:",Ret)

    
    Ret = subtraction(A,B)
    print("subtraction is:",Ret)

    if __name__ == "__main__":
        main()
