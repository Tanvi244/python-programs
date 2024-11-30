
def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum




def main():
    print("enter no of element u want insert list")
    size = int(input())


    Arr = list()

    print("enter ele")

    for i in range(size):
        no = int(input())
        Arr.append(no)

        
     print("enter element",Arr)


   


     Result = Addition(Arr)
     print("summation:",Result)





if __name__ = "__main__":
    main()