def run():
    a=18
    b=16
    c=27
    total=a+b+c
    recessive=((c/total)*((c-1)/(total-1)))
    hetero=(.25)*((b/total)*((b-1)/(total-1)))
    both=(b/total)*(c/(total-1))
    print(recessive)
    print(hetero)
    print(both)
    print(1-recessive-hetero-both)
