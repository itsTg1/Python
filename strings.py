#strings

# len endswith count capatalize lower upper stripe title find index replace split

string=input("enter the string")
print(len(string),end="\n")

cnt=0
for i in range(0,len(string)):

    if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
        cnt=cnt+1

print(cnt)
temp=string
string=string[-1::-1]
print(string)

if string==temp:
    print("pallindrome")
else:
    print("not pallindrome")

print(temp.upper())
print(temp.lower())

print(temp.find('l'))

new=string.replace(" ","_")
print(new)

if temp[0]==temp[-1]:
    print("start and end with same char")
else:
    print("no")

print(len(temp.split(" ")))

for i in range(0,len(string)):

    if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
        string=string.replace(string[i],'*')

print(string)


str1=input("enter string 2 \n")
str2=input("enter string 3 \n")
arr1=list(str1)
arr2=list(str2)
arr1.sort()
arr2.sort()
if arr1==arr2:
    print("anagram")
else:
    print("no anagram")


newStr=str1+str2
print(newStr)

punc="hi,are you there?"
arr=list(punc)
newpunc=""
for i in range(0,len(punc)):
    if arr[i] not in [',', '?', '!']:
        newpunc=newpunc+arr[i]
    else:
        continue

print(newpunc)

frq=[]
dic={}
for i in range(0,len(string)):
    if string[i] not in frq:
        frq.append(string[i])
        dic.update({string[i]:string.count(string[i])})

print(dic.items())

# Swap the case of each character in a string (uppercase to lowercase and vice versa).

swapStr=""
for i in range(0,len(temp)):
    if temp[i:i+1].isupper():
        swapStr+=temp[i].lower()
    else:
        swapStr+=temp[i].upper() 

print(swapStr)

# program to find all the unique characters in a string
unique=[]
for i in range(0,len(string)):
    if temp[i] not in unique and temp[i]!=' ':
        unique.append(temp[i])
        
print(unique)

# Extract the username from an email address (e.g., for user123@gmail.com, return user123).
email="trinaan1223@gmail.com"
print(email.split('@')[0])

# checks if a string contains only digits.
checkStr="2321"
print(checkStr.isnumeric())

# all duplicate characters from a string
dupStr="abbacefde"
isPresent=[]
newStr1=""
for i in range(0,len(dupStr)):
    if dupStr[i] not in isPresent:
        isPresent.append(dupStr[i])
        newStr1+=dupStr[i]

print(newStr1)

# Count how many times each word appears in a string
stringWord="hello hello you are not well not"
words=stringWord.split(" ")
frq=[]
dic1={}
for i in range(0,len(words)):
    if words[i] not in frq:
        frq.append(words[i])
        dic1.update({words[i]:words.count(words[i])})

print(dic1.items())

# Compress a string using run-length encoding
sample="aabcccccaaa"
i=0
ans=""
while i<len(sample):
    ele=sample[i]
    cnt=0
    while(i<len(sample) and sample[i]==ele):
        cnt+=1
        i+=1
    ans+=ele
    ans+=str(cnt)

print(ans)

# Find the longest word in a sentence.
words.sort(key=len,reverse=True)
print(words[0])

# Write a program to check if all characters in a string are unique
unique1=[]
ans1=True
for i in range(0,len(temp)):
    if temp[i] not in unique1 and temp[i]!=' ':
        unique1.append(temp[i])
    elif temp[i] in unique1 and temp[i]!=' ':
        ans1=False
if(ans1):
    print("all unique")
else:
    print("not unique")

# Implement a custom title case converter (capitalize first letter of each word).
def titleCaseConvertor(heading):
    heading=heading.title()
    return heading

title=titleCaseConvertor("story of my life")
print(title)

# Remove all occurrences of a substring from a string
substr = "abc"
example = "abcdefaczxabc"

while substr in example:
    idx = example.find(substr)
    example = example[:idx] + example[idx + len(substr):]

print(example)

# strip
strspaces="  hue "
print(strspaces.strip())