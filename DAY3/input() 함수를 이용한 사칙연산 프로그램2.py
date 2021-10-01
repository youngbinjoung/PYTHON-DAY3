# 메뉴 만들기 - 사칙 연산 기능 추가 구현

# 원하는 기능을 선택해주세요 (1. 더하기, 2. 빼기, 3. 곱하기, 4. 나누기): 2
# 첫번째 숫자를 입력해주세요 : 12
# 두번째 숫자를 입력해주세요 : 30
# 12 - 30 = -18


choice=int(input("원하는 기능을 선택해주세요 (1.더하기, 2. 빼기, 3. 곱하기,4. 나누기): "))
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
