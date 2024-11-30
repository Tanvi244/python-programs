from functools import reduce#package
'''def CheckEven(No):#check even or odd
    return (No % 2 == 0)'''

CheckEven = lambda No : (No% 2 == 0)

Increase = lambda No : No + 1

Add = lambda A,B :  A+B



def main():
    Data = [11,14,20,23,18,16,15,20]#input list
    print("data from input list:",Data)

    FData = list(filter(CheckEven,Data))#filter
    print("data after filter activity",FData)


    MData = list(map(Increase,FData))#map 11 value vadhavnar 11 asel tar 12 karnar
    print("data after map activity:",MData)


    RData = reduce(Add,MData)#reduce  #add kela map cha data so mdata ghetla
    print("data after reduce activity:",RData)


if __name__ == "__main__":
    main()

