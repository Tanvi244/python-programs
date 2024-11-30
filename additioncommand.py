import sys  #asa command line pramane code jo industria;l lagto company la interview dyal teva addition program

def Addition(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    print("welcome appli"+sys.argv[0])


    if(len(sys.argv)  != 3):
        print("invalid no arg")
        print("provide 2 numeric arg perform addition")
        return


        Result = Addition(int(sys.argv[1]), int(sys.argv[2]))

        print("add is: ",Result)


if __name__ == "__main__":
    main()
