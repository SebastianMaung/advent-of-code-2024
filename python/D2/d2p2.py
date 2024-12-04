a = open("2024\python\D2\d2data.txt")
b=""
num = ""
safe = 0
z= 0
content = list(a.readlines())
#print(content[0])
mistaketotal = 0
def check2(theinput):
    temp = theinput
    mistake = 0
    for z in range(len(theinput)):
        try:
            mlist.pop(z)  
        except IndexError:
            break
        for j in range(len(theinput) - 1):  
            print(theinput[j], theinput[j+1])
            if theinput[j] - theinput[j+1] > 4 and theinput[j+1] != theinput[0]:
                print("BAD 3")
                mistake += 1
                #safe = safe - 1

            if theinput[j+1] - theinput[j] > 4 and theinput[j+1] != theinput[:1]:
                #print(mlist[j])
                mistake += 1
                print("BAD 4")
                #safe = safe - 1
                break
        theinput = temp
    if mistake > 0:
        return "UNSAFE"

    #print("safe")

for i in range (len(content)):
    #print(content[i])
    old = safe
    mlist = content[i].split(" ")
    mlist = [int(i) for i in mlist]
    #print(mlist)
    INCREASING = None
    DECREASING = None
    for x in range (len(mlist)):
        try: 
            mlist[x+1]
        except IndexError:
            print("safe")
            safe += 1
            break

        if mlist[x] - mlist[x+1] > 4 and mlist[x+1] != mlist[:1]:
            print(mlist[x])
            print("BAD 3")
            break
        if mlist[x+1] - mlist[x] > 4 and mlist[x+1] != mlist[:1]:
            print(mlist[x])
            print("BAD 4")
            break
        if old == safe: #are you sure????
            if check2(mlist) == "UNSAFE":
                break
    #print("safe")



print(safe)