class complex:
    # static member
    iotaval=-1
    # private member
    __isComplex=True

    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary
    def __str__(self):
        return str(f"{self.real}+{self.imaginary}i")
    def print(self):
        print(f"{self.real}+{self.imaginary}i")
    def __add__(self,comp):
        realPart=self.real+comp.real
        imagiPart=self.imaginary+comp.imaginary
        return complex(realPart,imagiPart)
    def __sub__(self,other):
        realPart=self.real-other.real
        imgPart=self.imaginary-other.imaginary
        return complex(realPart,imgPart)
    def __eq__(self, other):
        if self.real==other.real and self.imaginary==other.imaginary:
            return True
        else:
            return False
    def __gt__(self,other):
        val1=((self.real)**2 + (self.imaginary)**2)**(0.5)
        val2=((other.real)**2 + (other.imaginary)**2)**(0.5)
        return val1>val2

num1=complex(3,4)
num2=complex(3,9)
num3=complex()
print(num1)
print(num2)
print(num2-num1)
print(num2+num1)
print(num1==num2)
if(num1>num2):
    print("num1 is greater than num2")
else:
    print("num2 is greater than num1")

# do nothing as this condition is true
assert num2>num1

# throws an assertion error
assert num1>num2


'''
In Python, constructors (__init__ methods) are inherited by default — but with a catch:

If the child class does not define its own __init__, 
it will automatically use the parent’s __init__.

If the child class does define its own __init__, it 
overrides the parent’s, and you must explicitly call the parent’s constructor 
using super().__init__() if you still want its initialization logic to run.

super() -> it is only used to access parent methods and not attributes
'''