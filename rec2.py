import sys

def main():
    print("recursion limit :",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("recursion limit :",sys.getrecursionlimit())


if __name__ == "__main__":
        main()