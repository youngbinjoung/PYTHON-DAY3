# n부터 m까지의 수중 3의 배수이거나 7의 배수인 수들의 합 구하기

# 이 값들을 바꿔가면서 실행해주세요
n = 12
m = 100
num=0
key1=0
key2=0

while n<=m:
    if n%3==0 or n%7==0:
        key1=key1+n
    n+=1
print(key1)


