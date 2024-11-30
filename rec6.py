i = 1

def DisplayR():
    global i

    if(i <=5):
        print(i)
        DisplayR()
        i = i + 1
    

def main():
    DisplayR()
    


if __name__ == "__main__":
        main()