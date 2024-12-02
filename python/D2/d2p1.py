a = open("d2data.txt")
b=""
safe = 0
num = ""
z= 0
content = list(a.readlines())
#print(content[0])

for i in range (len(content)):
    #print(content[i])
    mlist = content[i].split(" ")
    mlist = [int(i) for i in mlist]
    print(mlist)
    INCREASING = None
    DECREASING = None
    for x in range (len(mlist)):
        try: 
            mlist[x+1]
        except IndexError:
            print("safe")
            safe += 1
            break
        if mlist[x] - mlist[x+1] > 0 and mlist[x+1] != mlist[:1]:
            #print("decreasing")
            DECREASING = True
        if mlist[x] - mlist[x+1] < 0 and mlist[x+1] != mlist[:1]:
            #print("increasing")
            INCREASING = True
        if DECREASING == True and INCREASING == True:
            print("BAD 1")
            break
        if mlist[x] - mlist[x+1] == 0 and mlist[x+1] != mlist[:1]:
            print(mlist[x])
            print("BAD 2")
            break
        if mlist[x] - mlist[x+1] > 3 and mlist[x+1] != mlist[:1]:
            print(mlist[x])
            print("BAD 3")
            break
        if mlist[x+1] - mlist[x] > 3 and mlist[x+1] != mlist[:1]:
            print(mlist[x])
            print("BAD 4")
            break
        if INCREASING == True and DECREASING == True:
            print("BAD 5")
            break
    #print("safe")


print(safe)