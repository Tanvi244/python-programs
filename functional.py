print("demo of functional")

Addition = lambda No1, No2 : No1 + No2

subtraction = lambda No1, No2 : No1 - No2
    
print("enter first no:")
A = int(input())

print("enter sec no :")
B = int(input())

Ret = Addition(A,B)
print("addition is:",Ret)

    
Ret = subtraction(A,B)
print("subtraction is:",Ret)



   
       
