#프로그램 반복하고 종료


while(1) :
    choice=int(input("원하는 기능을 선택해주세요 (1.더하기, 2. 빼기, 3. 곱하기,4. 나누기,5. 종료): "))
    if choice==5 :
        break
    
    num1=int(input("첫번째 숫자를 입력해주세요 :"))
    num2=int(input("두번째 숫자를 입력해주세요 :"))

    if choice==1 :
       print("{} + {} = {}".format(num1,num2,num1+num2))
    elif choice==2 :
       print("{} - {} = {}".format(num1,num2,num1-num2))
    elif choice==3 :
       print("{} X {} = {}".format(num1,num2,num1*num2))
    elif choice==4 :
       print("{} / {} = {}".format(num1,num2,num1/num2))
print("종료")
    

