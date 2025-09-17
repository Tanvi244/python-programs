def sub(A, B):      
    print(A - B)   # Original subtraction function

def SmartSub(fptr):     
    def Inner(A, B):
        if A < B:
            A, B = B, A
        return fptr(A, B)
    return Inner

# Wrap the sub function with SmartSub to create a new version of sub
sub = SmartSub(sub)

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    sub(No1, No2)  # Call the wrapped subtraction function

if __name__ == "__main__":
    main()


