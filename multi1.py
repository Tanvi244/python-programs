import os
def main():
    print("pid running process:",os.getpid())
    print("pid process command :",os.getppid())



if __name__ == "__main__":
    main()