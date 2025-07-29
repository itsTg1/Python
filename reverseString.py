def reverseString(s):
    #code here
    lis=[]
    length=len(s)
    for i in range(0,length):
        lis.append(s[i])
    lis.reverse()
    temp=""
    for i in range(0,length):
        temp=temp+lis[i]
    
    s=temp
    return s
