import multiprocessi

def Cube(No):
    return No*No*No

def main():
    Arr = [10,20,30,40]
    Result = []

    p = multiprocessing.pool()
    Result = p.map(Cube,Arr)
    p.close()
    p.join()



    print(Result)
   


    
if __name__ == "__main__":
    main()