def run(filename):
    f=open(filename)
    text=f.readlines()
    t=0
    total=0 
    for i in range(0,len(text)):
        if text[i][0]==">":
            #t=0
            print(">>>"+text[i])
            if t!=0:
                print(t)
                print(total)
                print(100*t/total)
            t=0
            total=0
        else:
            for a in range(0,len(text[i])):
                if text[i][a]=="G" or text[i][a]=="C":
                    t=t+1;
                    total=total+1;
                elif text[i][a]=="A" or text[i][a]=="T":
                    total=total+1;
#                print(text[i][a])
        #print (t)
