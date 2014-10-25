def run(filename):
    f=open(filename)
    text=f.readlines()
    t=-1
    total=0
    list1=list()
    for i in range(0,len(text)):
        if text[i][0]==">":
            t=t+1
            a=0
        else:
            #for a in range(0,len(text[i])):
            a=a+1
            if a==1:
                list1.append(text[i].rstrip())
            else: list1[t]=list1[t]+text[i].rstrip()
                #print(list1[t])
    print(list1)
    """
    for i in range (0,len(list1)):
        print list1[i]
    """
