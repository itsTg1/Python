import re
# print its contents line by line
with open("notes.txt","r") as f:
    data=f.readline()
    lines=0
    while data:
        print(data)
        lines+=1
        data=f.readline()

# count lines
print(lines)

# count the words
with open("notes.txt","r") as f:
    data=f.read()
    lis=re.split(r'[ .?|,]+',data)
    print(lis[:len(lis)-1])
    print(len(lis)-1)
    # count chars
    cnt = 0
    for ch in data:
        if ch not in [" ", "\n", "\t"]:  # ignore whitespace
            print(ch, end=",")
            cnt += 1
    print("\nTotal chars:", cnt)


# Copy File
with open("notes.txt","r") as f:
    data = f.read()
    with open("copy.txt","w") as f1:
        f1.write(data)


# Write User Input && Append to File
with open("user.txt","a") as f:
    for i in range(0,4):
        line=input(f"enter {i+1} line")
        f.write(line + "\n")


# replace word
with open("notes.txt","r") as f:
    data = f.read()

data = data.replace("is", "are")

with open("notes.txt","w") as f:   # open in write mode, not r+
    f.write(data)

