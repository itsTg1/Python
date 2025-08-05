# immutable
tup=(1,)
print(type(tup))

# Write a program to convert a list into a tuple
lis=[1,2,22,442,23]
tup1=tuple(lis)
print(tup1)

# Check whether an item exists in a tuple
print(23 in tup1)

#  length of a tuple
print(len(tup1))

# Concatenate two tuples
tup_con=tup1+tup
print(tup_con)

# Repeat a tuple 3 times 
tup3=tup1*3
print(tup3)

# Convert a tuple of strings into a single string
final=""
string=("jimmy","is","going","to","park")
for i in range(0,len(string)):
    final+=string[i];
print(final)

# method-2
string = ("jimmy", "is", "going", "to", "park")
final = " ".join(string)  # More efficient and readable
print(final)


# Unpack the values of a tuple into separate variables

a,b,c,d,e=("jimmy","is","going","to","park")
print(e)

# Swap two tuples
temp=string
string=tup1
tup1=temp
print(string)

#  index of an element
print(string.index(442))

# how many times an element appears in a tuple
print(tup_con.count(1))

# Convert a nested tuple into a list of lists
tup_nested=(1,(1,2))
lis_nes=[]
for i in range (0,len(tup_nested)) :
    if(type(tup_nested[i])==tuple):
        lis_nes.append(list(tup_nested[i]))
    
    else:
        lis_nes.append(tup_nested[i])

print(lis_nes)

# Sort a tuple of integers in descending order
tup_sort=(22,3,12,442,21)
lis1=list(tup_sort)
lis1.sort(reverse=True)
tup_sort=tuple(lis1)
print(tup_sort)

# slice a tuple from index 2 to 5
print(tup_sort[1:4])

# Check whether two tuples have at least one common element
cnt=0
for i in range(0,len(tup_sort)):
    if tup_sort[i] in string:
        cnt+=1
if(cnt>=1):
    print(f"{cnt} common")

else:
    print("no common")

# program to remove duplicate elements from a tuple
appeared=[]
tup_dup=(22,1,11,299,232,22,11,4,1)
for i in range(0,len(tup_dup)):
    if tup_dup[i] not in appeared:
        appeared.append(tup_dup[i])

tup_dup=tuple(appeared)
print(tup_dup)

# Flatten a tuple of tuples
t=((1, 2), (3, 4), (5, 6))
l=[]
for i in range(0,len(t)):
    if(type(t[i])==tuple):
        for j in range(0,len(t[i])):
            l.append(t[i][j])
    else:
        l.append(t[i])
t=tuple(l)
print(t)

# tuple of key-value pairs to a dictionary

dict={}
tup_pair=(("jimmy",24),("harsh",25),("kaushal",12))
for i in range(0,len(tup_pair)):
    a,b=tup_pair[i]
    print(a)
    dict.update({a:b})
print(dict)

# sum
tup_nums = (10, 20, 30, 40)
total = sum(tup_nums)
print(total)

# Convert tuple of strings to a string with custom separator
tup_strs = ("hello", "python", "world")
joined = "-".join(tup_strs)
print(joined)
