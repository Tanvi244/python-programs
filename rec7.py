

i = 1

def DisplayR():
    global i

    if(i <=5):
        print(i)
         i = i + 1
         DisplayR()

    

def main():
    print("enter no:")
    value = int(input())
    DisplayR(value)
    


if __name__ == "__main__":
        main()