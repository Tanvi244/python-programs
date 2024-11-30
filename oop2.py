
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

    @classmethod#decorator
    def Fun(cls):
        print("value of data1 from fun:",Demo.Data1)
        print("value of data1 from fun:",Demo.Data2)

    @staticmethod
    def Gun():
        print("static method")
      
Demo.Fun()
Demo.Gun()
obj1 = Demo(5,10)

obj1.Display()


