print("Hello World!")
# single line

'''multiline commenent '''

# no data type in front of variable

name="triyan"
print("name",name)

# indentation is neccessary in python 

# no curly braces needed
age=30
if age==30:
    print("eligible to vote")

#line continuation 

total= 1+2+3+4\
+5+6

print (total)

# multiple statements in a line

z=4;y=9;x=z+y
print(x);

# use type--Inference <class 'int' 'str'>
type(x)

# declaring variables
amit=""
print(amit)

# naming convention -- start from letter or underscore and digit between 

# type of variable is determined at run time

# converting data type and cando multiple conversions

age_str=str(age);
print(age_str)
print(type(age_str))

# dynamic typing

var=90
var="triyan gupta"

ip=input("type the value")
print(ip)

# advanced datatypes -> lists, tuples,dictionaries,sets
# gives false
print(bool())

# error--->> strr="get value"+9

# floor division -->normal gives 2.5
print(5//2)

# exponential 
5**2

# and or not 

# conditional statements --> if else elif

if age>=18:
    print("elegible to vote")
elif age==30:
    print("sorry not elegible")
else:
    print("underage")


# nested
if age>7:
    if name=="triyan":
        print("my child")

# loops---> iterating over range

for i in range(0,7):
    print(i);

for i in range(4):
    print(i)

# through string
for i in var:
    print(i)

# while
k=0;
while k<3:
    print("still in loop")
    k+=1;


# pass-->null operation it does nothing

# lists--> ordered and mutable and hetrogeneous

lst=["krish","hello",3.14,True];

# accessiing elements of lists --> list_name[idx]

print(lst[1::2])

lst[1:]="salman"
# ['krish', 's', 'a', 'l', 'm', 'a', 'n']
print(lst[:])

# at last append 
lst.append("cherry");

# at specific index--->> insert(idx no. , element_to_insert)
lst.insert(1,"banana")

# remove and return last --> pop()

# to get index of an element-->> index of banna is:- 1

print("index of banna is:-",lst.index("banana"))

lst.reverse();

# clear entire list or remove all elments
lst.clear();

# iterating over list
for i in lst:
    print(i);

# other way to iterate with indexes

for index,i in enumerate(lst):
    print(index,i);


# list comprehension---> syntax [expression for item in iterable if condition]
newlst=[]
for x in range(1,3):
    newlst.append(x*x)

# above is same as

[x**x for x in range(10)];

# [0, 2, 4]
evenlist=[x for x in range(6) if x%2==0]
print(evenlist)

lst1=[1,2,3]
lst2=[4,5]
# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
lst3=[(i,j) for i in lst1 for j in lst2]
print(lst3)