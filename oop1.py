class Demo:
    Data1 = 11
    Data2 = 21

    def __init__(self, A, B):#a madhe 5 copy honar b madhe 10
        print("inside constructor")
        self.No1 = A #instance variable
        self.No2 = B#instance aria

    def Display(self):#instance method
        print("value from No1 from Display",self.No1)#behaviour
        print("value from No2 from Display",self.No2)
        print("value from No2 from Display",Demo.Data1)#11 11 21 milnar cha 
        print("value from No2 from Display",Demo.Data2)#21


obj1 = Demo(5,10)

obj2 = Demo(15,20)#b madhe janar 20 a madhe 15

print("value of no1 from obj1 :",obj1.No1) #5
print("value of no2 from obj1 :",obj1.No2) #10

print("value of no1 from obj2 :",obj2.No1) #15
print("value of no2 from obj2 :",obj2.No2)#20

print("value of Data1 :",Demo.Data1)
print("value of Data2 :",Demo.Data2)

obj1.Display()
obj2.Display()