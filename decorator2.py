def sub(A,B):
    print(A/B)


def SmartSub(fptr):
    def Inner(A,B):
        if A < B:
            A,B = B,A#swap kela
        return fptr(A,B)
    return Inner

sub = SmartSub(sub)

def main():
    No1 = int(input("enter first no:"))
    No2 = int(input("enter sec no:"))

    sub(No1,No2)






if __name__ == "__main__":
    main()