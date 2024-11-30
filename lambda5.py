def Even(A):
    return (A%2 == 0)

Even = lambda A :(A%2 == 0)
   
    


def main():
    Ret = Even(11)
    if(Ret == True):
        print("even no")
    else:
        print("odd no")
  
    

if __name__ == "__main__":
    main()