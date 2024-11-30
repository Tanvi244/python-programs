print("demo of oop")

class Arithmetic:
    def__init__(self,value1, value2):#constructor
        self.No1 = value1#characteristics
        self.No2 = #characteristics
        


    def__init__(self,value1,value2):
        self.No1 = value1
        self.No2 = value2 

    def Addition(self):#behaviour
        Ans = self.No1 + self.No2
        return Ans

    
    def subtraction(self):#behaviour
        Ans = self.No1 - self.No2
        return Ans





print("enter first no:")
A = int(input())

print("enter sec no :")
B = int(input())

obj = Arithmetic(A,B)


Ret = obj.Addition()
print("addition is:",Ret)

    
Ret = obj.subtraction()
print("subtraction is:",Ret)
