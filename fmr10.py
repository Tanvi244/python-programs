import marvellousfmr
def main():
    Data = []#input list
    print("enter ele")
    size = int(input())
    print("enter elements ")
    iCnt = 0

    for iCnt in range(0,size):
        No = int(input())
        Data.append(No)

        print("data from input list:",Data)

        

    FData = list(filterX(CheckEven,Data))#filter
    print("data after filter activity",FData)


    MData = list(mapX(Increase,FData))#map 11 value vadhavnar 11 asel tar 12 karnar
    print("data after map activity:",MData)


    RData = reduceX(Add,MData)#reduce  #add kela map cha data so mdata ghetla
    print("data after reduce activity:",RData)


if __name__ == "__main__":
    main()

