y = 7
star=6
x=1
a=1
num1=1
num2=1
while a<=y :
    while x<=star:
     print(" ", end="")
     x+=1
    while num1<=num2 :
        print("*",end="")
        num1+=1
    print("")
    star=star-1
    a+=1
    x=1
    num1=1
    num2+=1

# 출력
'''

  *
 **
***

'''

y = 5
# 출력
'''

    *
   **
  ***
 ****
*****

'''

y = 7
# 출력
'''

      *
     **
    ***
   ****
  *****
 ******
*******

'''

