# Create a class Vector with attributes x and y.

# Overload the + operator to add two vectors.

# Overload the == operator to check equality.

class Vector:
    def __init__(self,x):
        self.x=x
    
    def __str__(self):
        p="".join(str(self.x))
        return p

    
    def __add__(self,other):
        temp=[]
        for i in range(0,min(len(self.x),len(other.x))):
            temp.append(self.x[i]+other.x[i])
        
        if(len(self.x)>len(other.x)):
            temp=temp+self.x[len(other.x):len(self.x)]
        else:
            temp=temp+other.x[len(self.x):len(other.x)]
        return Vector(temp)
    
    def __eq__(self, other):
        return (self.x==other.x)

v1=Vector([2,3,4,5])
v2=Vector([2,3,1])
v3=v1+v2
print(v3)
print(v1==v2)