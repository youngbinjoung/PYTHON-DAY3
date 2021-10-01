
gugu=2
while gugu<9 :
    gugu+=1
    dan=1
    print("=={}단==".format(gugu))
    while dan<9 :
        dan+=1
        if dan%2==0 :
            print("{} x {} = {}".format(gugu,dan,gugu*dan))
        
        
