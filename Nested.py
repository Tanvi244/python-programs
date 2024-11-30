def Calculations(No1, No2):

    def Addition(X, Y):
        return X+Y

        def Subtraction(X,Y):
            return X-Y
             Ans1 = Addition(No1, No2)
            
            Ans2 = Subtraction(No1, No2)
                  return Ans1,Ans2
       
      
        



 


 



print("enter fir no")
A = int(input())


print("enter sec no")
B = int(input())

Result1, Result2 = Calculations(A, B)


print("Add is : ",Result1)

print("sub is : ",Result2)
