

i = 1

def DisplayR(no):
    global i

    if(no >= 1):
        print(no)
        no = no - 1
        DisplayR(no)

    
def main():
    print("enter no:")
    value = int(input())


    DisplayR(value)
    


if __name__ == "__main__":
        main()