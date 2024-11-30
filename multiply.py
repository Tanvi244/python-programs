def Calculations(No1, No2):

    
Add = No1 + No2
Sub = No1 - No2
return = Add, Sub




print("enter fir no")
A = int(input())


print("enter sec no")
B = int(input())

Result1, Result2 = Calculations(A, B)


print("Add is : ",Result1)

print("sub is : ",Result2)
