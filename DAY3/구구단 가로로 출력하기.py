#구구단 가로

a=2
dan=1
while a<10:
    gugu=2
    a+=1
    while gugu<10 :
        print("{} x {} = {}".format(gugu,dan,gugu*dan), end="\t")
        gugu+=1
    print()
    dan+=1
    
        
